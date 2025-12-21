// Cloudflare Worker for handling contact form submissions and emailing them out via MailChannels
// Configure environment variables in Wrangler:
// - TARGET_EMAIL (required): where leads should be sent (e.g., leads@example.com)
// - FROM_EMAIL (optional, but should be an address on your domain, e.g., web@liongaragedoors.ca)
// - ALLOWED_ORIGINS (optional): comma-separated list of allowed origins for CORS. Defaults to liongaragedoors.ca + www.
export default {
  async fetch(request, env) {
    const allowedOrigins = getAllowedOrigins(env);
    const cors = buildCorsHeaders(request, allowedOrigins);

    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: cors });
    }

    if (request.method !== 'POST') {
      return new Response(JSON.stringify({ error: 'Method not allowed' }), { status: 405, headers: cors });
    }

    const origin = request.headers.get('Origin');
    if (origin && !allowedOrigins.includes(origin)) {
      return new Response(JSON.stringify({ error: 'Origin not allowed' }), { status: 403, headers: cors });
    }

    const payload = await parseBody(request);
    if (!payload) {
      return new Response(JSON.stringify({ error: 'Invalid or missing body' }), { status: 400, headers: cors });
    }

    const name = truncate(payload.name || 'N/A', 200);
    const phone = truncate(payload.phone || 'N/A', 50);
    const email = truncate(payload.email || 'N/A', 200);
    const message = truncate(payload.message || 'N/A', 5000);
    const source = truncate(payload.source || request.headers.get('Referer') || 'unknown', 500);
    const ip = request.headers.get('CF-Connecting-IP') || 'unknown';
    const ua = truncate(request.headers.get('User-Agent') || 'unknown', 500);

    if (!env.TARGET_EMAIL) {
      return new Response(JSON.stringify({ error: 'TARGET_EMAIL is not set' }), { status: 500, headers: cors });
    }

    const textBody = [
      'New contact form submission',
      `Name: ${name}`,
      `Phone: ${phone}`,
      `Email: ${email}`,
      `Message: ${message}`,
      `Source/Page: ${source}`,
      `IP: ${ip}`,
      `User-Agent: ${ua}`
    ].join('\n');

    const fromEmail = env.FROM_EMAIL || `web@liongaragedoors.ca`;

    const mailPayload = {
      personalizations: [
        {
          to: [{ email: env.TARGET_EMAIL }]
        }
      ],
      from: {
        email: fromEmail,
        name: 'Lion Garage Doors Website'
      },
      subject: `New website lead from ${name || 'visitor'}`,
      content: [
        {
          type: 'text/plain',
          value: textBody
        }
      ]
    };

    const mailResp = await fetch('https://api.mailchannels.net/tx/v1/send', {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify(mailPayload)
    });

    if (!mailResp.ok) {
      const errText = await mailResp.text();
      return new Response(JSON.stringify({ error: 'Email failed', details: errText }), { status: 502, headers: cors });
    }

    return new Response(JSON.stringify({ ok: true }), { status: 200, headers: cors });
  }
};

function truncate(value, max) {
  return String(value || '').slice(0, max);
}

async function parseBody(request) {
  const contentType = request.headers.get('content-type') || '';
  if (contentType.includes('application/json')) {
    try {
      return await request.json();
    } catch {
      return null;
    }
  }
  if (contentType.includes('application/x-www-form-urlencoded') || contentType.includes('multipart/form-data')) {
    const form = await request.formData();
    return Object.fromEntries(form.entries());
  }
  return null;
}

function getAllowedOrigins(env) {
  if (env.ALLOWED_ORIGINS) {
    return env.ALLOWED_ORIGINS.split(',').map((o) => o.trim()).filter(Boolean);
  }
  return ['https://liongaragedoors.ca', 'https://www.liongaragedoors.ca'];
}

function buildCorsHeaders(request, allowedOrigins) {
  const origin = request.headers.get('Origin');
  const headers = {
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '86400'
  };
  if (origin && allowedOrigins.includes(origin)) {
    headers['Access-Control-Allow-Origin'] = origin;
  } else {
    headers['Access-Control-Allow-Origin'] = allowedOrigins[0];
  }
  return headers;
}

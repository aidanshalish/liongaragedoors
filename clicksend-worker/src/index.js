export default {
  async fetch(request, env, ctx) {
    if (request.method !== "POST") {
      return new Response("Only POST allowed", { status: 405 });
    }

    const { name, email, phone, service } = await request.json();

    const msg = `New Consultation Request:
Name: ${name}
Email: ${email}
Phone: ${phone}
Service: ${service}`;

    const body = {
      messages: [{
        source: "web",
        body: msg,
        to: "+14164541776", // e.g. +11234567890
      }]
    };

    const auth = btoa(`${env.CLICKSEND_USER}:${env.CLICKSEND_API_KEY}`);

    const res = await fetch("https://rest.clicksend.com/v3/sms/send", {
      method: "POST",
      headers: {
        "Authorization": `Basic ${auth}`,
        "Content-Type": "application/json"
      },
      body: JSON.stringify(body)
    });

    if (!res.ok) {
      return new Response("Failed to send SMS", { status: 500 });
    }

    return new Response("Request sent via SMS successfully!");
  }
};


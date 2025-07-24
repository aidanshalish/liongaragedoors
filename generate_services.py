#!/usr/bin/env python3
"""
Service Cards Generator for Lion Windows and Doors
Uses OpenAI to generate HTML service cards based on available services
"""

import os
import sys
from openai import OpenAI

def main():
    # Check if API key is available
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set.")
        sys.exit(1)
    
    # Initialize the OpenAI client
    client = OpenAI(api_key=api_key)
    
    # Available services from the services/ directory
    services = [
        {
            "name": "Casement Windows",
            "file": "casement_window.html",
            "description": "Reliable casement window installation and repair services"
        },
        {
            "name": "Closet Doors", 
            "file": "closet_doors.html",
            "description": "Custom closet door solutions for better organization"
        },
        {
            "name": "Exterior Doors",
            "file": "exterior_doors.html", 
            "description": "Secure and stylish exterior door installation"
        },
        {
            "name": "Glass Replacement",
            "file": "glass_replacement.html",
            "description": "Professional glass replacement and repair services"
        },
        {
            "name": "Patio Doors",
            "file": "patio_doors.html",
            "description": "Smooth and stylish patio door installation and repair"
        },
        {
            "name": "Weatherstripping & Sealing",
            "file": "weatherstripping_sealing.html",
            "description": "Energy-efficient weatherstripping and sealing solutions"
        }
    ]
    
    print("🔧 Generating service cards using OpenAI...")
    
    try:
        # Create the prompt for OpenAI
        services_info = "\n".join([f"- {s['name']}: {s['description']}" for s in services])
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system", 
                    "content": "You are a web developer creating HTML service cards for a windows and doors company. Create professional, consistent HTML cards that match the existing design patterns."
                },
                {
                    "role": "user", 
                    "content": f"""Create 6 HTML service cards for these Lion Windows and Doors services:

{services_info}

Requirements:
1. Each card should follow this structure:
   - Card wrapper with class="card bg-white"
   - Image with appropriate Unsplash URL (related to the service)
   - Service icon with FontAwesome class
   - Service title (h3 with proper classes)
   - Brief description paragraph
   - 3 bullet points with checkmark icons
   - "Get a Quote" button linking to #contact

2. Use these CSS classes consistently:
   - Cards: "card bg-white"
   - Images: "w-full h-48 object-cover"
   - Icons: "service-icon mx-auto" with FontAwesome icons
   - Titles: "text-xl font-semibold mb-3 text-center"
   - Descriptions: "text-gray-600 mb-4 text-center"
   - Lists: "space-y-2 mb-4"
   - List items: "flex items-start"
   - Checkmarks: "fas fa-check text-yellow-500 mt-1 mr-2"
   - Buttons: "btn-primary w-full block text-center mt-4"

3. Choose appropriate FontAwesome icons for each service
4. Write professional, benefit-focused descriptions
5. Include realistic features/benefits for each service
6. Use high-quality Unsplash images related to each service

Format the output as clean HTML only, no explanations."""
                }
            ],
            max_tokens=2000,
            temperature=0.7
        )
        
        # Get the generated HTML
        generated_html = response.choices[0].message.content
        
        # Save to file
        with open('/Users/ubuntu/WebstormProjects/lionwindowsanddoors/generated_services.html', 'w') as f:
            f.write(generated_html)
        
        print("✅ Service cards generated successfully!")
        print("📁 Output saved to: generated_services.html")
        print("\n🎯 Next steps:")
        print("1. Review the generated content")
        print("2. Copy the HTML cards to replace the existing service cards in index.html")
        print("3. Update links to point to the correct service files")
        
        # Display the first few lines for preview
        print("\n📋 Preview of generated content:")
        print("=" * 50)
        print(generated_html[:500] + "..." if len(generated_html) > 500 else generated_html)
        
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

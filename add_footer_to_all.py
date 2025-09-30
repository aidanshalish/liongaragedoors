#!/usr/bin/env python3
"""
Script to add the consistent footer and JavaScript from index.html 
to all other HTML files in the Lion Windows and Doors project.
"""

import os
import re
from pathlib import Path

# Define the footer HTML and JavaScript content
FOOTER_HTML = '''
<!-- Footer -->
<footer id="contact" class="relative bg-gray-900 text-white overflow-hidden">
    <!-- Background Pattern -->
    <div class="absolute inset-0 opacity-5">
        <svg class="w-full h-full" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <pattern id="grid" width="10" height="10" patternUnits="userSpaceOnUse">
                    <path d="M 10 0 L 0 0 0 10" fill="none" stroke="currentColor" stroke-width="0.5"/>
                </pattern>
            </defs>
            <rect width="100" height="100" fill="url(#grid)" />
        </svg>
    </div>
    
    <!-- Main Footer Content -->
    <div class="relative pt-16 pb-8">
        <div class="container mx-auto px-4">
            <!-- Top Section -->
            <div class="grid grid-cols-1 lg:grid-cols-4 gap-8 mb-12">
                <!-- Company Info -->
                <div class="lg:col-span-2">
                    <div class="mb-6">
                        <div class="text-3xl font-bold mb-4">
                            <span class="text-yellow-500"><i class="fas fa-lion mr-2"></i>Lion</span>WindowsAndDoors
                        </div>
                        <p class="text-gray-300 text-lg mb-6 leading-relaxed">
                            Transforming homes across the GTA with premium window and door solutions since 2008. 
                            Your trusted partner for quality, security, and energy efficiency.
                        </p>
                        
                        <!-- Contact Info Cards -->
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-6">
                            <div class="bg-gray-800 rounded-lg p-4 border border-gray-700 hover:border-yellow-500 transition-colors duration-300">
                                <div class="flex items-center mb-2">
                                    <i class="fas fa-phone text-yellow-500 mr-3"></i>
                                    <span class="font-semibold">Call Us</span>
                                </div>
                                <a href="tel:+12898036671" class="text-gray-300 hover:text-yellow-500 transition-colors">
                                    (289) 803-6671
                                </a>
                            </div>
                            <div class="bg-gray-800 rounded-lg p-4 border border-gray-700 hover:border-yellow-500 transition-colors duration-300">
                                <div class="flex items-center mb-2">
                                    <i class="fas fa-envelope text-yellow-500 mr-3"></i>
                                    <span class="font-semibold">Email Us</span>
                                </div>
                                <a href="mailto:info@lionpro.ca" class="text-gray-300 hover:text-yellow-500 transition-colors">
                                    info@lionpro.ca
                                </a>
                            </div>
                        </div>
                        
                        <!-- Social Media -->
                        <div class="flex space-x-4">
                            <a href="#" class="w-10 h-10 bg-gray-800 rounded-full flex items-center justify-center hover:bg-yellow-500 transition-colors duration-300 group">
                                <i class="fab fa-facebook-f text-gray-300 group-hover:text-gray-900"></i>
                            </a>
                            <a href="#" class="w-10 h-10 bg-gray-800 rounded-full flex items-center justify-center hover:bg-yellow-500 transition-colors duration-300 group">
                                <i class="fab fa-instagram text-gray-300 group-hover:text-gray-900"></i>
                            </a>
                            <a href="#" class="w-10 h-10 bg-gray-800 rounded-full flex items-center justify-center hover:bg-yellow-500 transition-colors duration-300 group">
                                <i class="fab fa-google text-gray-300 group-hover:text-gray-900"></i>
                            </a>
                            <a href="#" class="w-10 h-10 bg-gray-800 rounded-full flex items-center justify-center hover:bg-yellow-500 transition-colors duration-300 group">
                                <i class="fab fa-linkedin-in text-gray-300 group-hover:text-gray-900"></i>
                            </a>
                        </div>
                    </div>
                </div>
                
                <!-- Quick Links -->
                <div>
                    <h3 class="text-xl font-bold mb-6 text-yellow-500">Quick Links</h3>
                    <ul class="space-y-3">
                        <li><a href="index.html" class="text-gray-300 hover:text-yellow-500 transition-colors duration-300 flex items-center"><i class="fas fa-chevron-right mr-2 text-xs"></i>Home</a></li>
                        <li><a href="index.html#about" class="text-gray-300 hover:text-yellow-500 transition-colors duration-300 flex items-center"><i class="fas fa-chevron-right mr-2 text-xs"></i>About Us</a></li>
                        <li><a href="index.html#services" class="text-gray-300 hover:text-yellow-500 transition-colors duration-300 flex items-center"><i class="fas fa-chevron-right mr-2 text-xs"></i>Our Services</a></li>
                        <li><a href="index.html#gallery" class="text-gray-300 hover:text-yellow-500 transition-colors duration-300 flex items-center"><i class="fas fa-chevron-right mr-2 text-xs"></i>Gallery</a></li>
                        <li><a href="index.html#testimonials" class="text-gray-300 hover:text-yellow-500 transition-colors duration-300 flex items-center"><i class="fas fa-chevron-right mr-2 text-xs"></i>Testimonials</a></li>
                        <li><a href="index.html#areas" class="text-gray-300 hover:text-yellow-500 transition-colors duration-300 flex items-center"><i class="fas fa-chevron-right mr-2 text-xs"></i>Service Areas</a></li>
                    </ul>
                </div>
                
                <!-- Services -->
                <div>
                    <h3 class="text-xl font-bold mb-6 text-yellow-500">Our Services</h3>
                    <ul class="space-y-3">
                        <li><a href="services/casement_window.html" class="text-gray-300 hover:text-yellow-500 transition-colors duration-300 flex items-center"><i class="fas fa-window-restore mr-2 text-sm"></i>Casement Windows</a></li>
                        <li><a href="services/exterior_doors.html" class="text-gray-300 hover:text-yellow-500 transition-colors duration-300 flex items-center"><i class="fas fa-door-open mr-2 text-sm"></i>Exterior Doors</a></li>
                        <li><a href="services/patio_doors.html" class="text-gray-300 hover:text-yellow-500 transition-colors duration-300 flex items-center"><i class="fas fa-door-open mr-2 text-sm"></i>Patio Doors</a></li>
                        <li><a href="services/glass_replacement.html" class="text-gray-300 hover:text-yellow-500 transition-colors duration-300 flex items-center"><i class="fas fa-glass-whiskey mr-2 text-sm"></i>Glass Replacement</a></li>
                        <li><a href="services/closet_doors.html" class="text-gray-300 hover:text-yellow-500 transition-colors duration-300 flex items-center"><i class="fas fa-door-closed mr-2 text-sm"></i>Closet Doors</a></li>
                        <li><a href="services/weatherstripping_sealing.html" class="text-gray-300 hover:text-yellow-500 transition-colors duration-300 flex items-center"><i class="fas fa-wind mr-2 text-sm"></i>Weatherstripping</a></li>
                    </ul>
                </div>
            </div>
            
            <!-- Service Areas Section -->
            <div class="border-t border-gray-700 pt-8 mb-8">
                <h3 class="text-xl font-bold mb-6 text-yellow-500 text-center">We Proudly Serve</h3>
                <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4 text-center">
                    <div class="text-gray-300 hover:text-yellow-500 transition-colors duration-300 py-2">
                        <i class="fas fa-map-marker-alt text-yellow-500 mr-1"></i>Aurora
                    </div>
                    <div class="text-gray-300 hover:text-yellow-500 transition-colors duration-300 py-2">
                        <i class="fas fa-map-marker-alt text-yellow-500 mr-1"></i>Markham
                    </div>
                    <div class="text-gray-300 hover:text-yellow-500 transition-colors duration-300 py-2">
                        <i class="fas fa-map-marker-alt text-yellow-500 mr-1"></i>Richmond Hill
                    </div>
                    <div class="text-gray-300 hover:text-yellow-500 transition-colors duration-300 py-2">
                        <i class="fas fa-map-marker-alt text-yellow-500 mr-1"></i>Vaughan
                    </div>
                    <div class="text-gray-300 hover:text-yellow-500 transition-colors duration-300 py-2">
                        <i class="fas fa-map-marker-alt text-yellow-500 mr-1"></i>Newmarket
                    </div>
                    <div class="text-gray-300 hover:text-yellow-500 transition-colors duration-300 py-2">
                        <i class="fas fa-map-marker-alt text-yellow-500 mr-1"></i>Barrie
                    </div>
                    <div class="text-gray-300 hover:text-yellow-500 transition-colors duration-300 py-2">
                        <i class="fas fa-map-marker-alt text-yellow-500 mr-1"></i>King City
                    </div>
                    <div class="text-gray-300 hover:text-yellow-500 transition-colors duration-300 py-2">
                        <i class="fas fa-map-marker-alt text-yellow-500 mr-1"></i>Georgina
                    </div>
                    <div class="text-gray-300 hover:text-yellow-500 transition-colors duration-300 py-2">
                        <i class="fas fa-map-marker-alt text-yellow-500 mr-1"></i>Bradford
                    </div>
                    <div class="text-gray-300 hover:text-yellow-500 transition-colors duration-300 py-2">
                        <i class="fas fa-map-marker-alt text-yellow-500 mr-1"></i>Innisfil
                    </div>
                    <div class="text-gray-300 hover:text-yellow-500 transition-colors duration-300 py-2">
                        <i class="fas fa-map-marker-alt text-yellow-500 mr-1"></i>Collingwood
                    </div>
                    <div class="text-gray-300 hover:text-yellow-500 transition-colors duration-300 py-2">
                        <i class="fas fa-map-marker-alt text-yellow-500 mr-1"></i>& More
                    </div>
                </div>
            </div>
            
            <!-- Call to Action Section -->
            <div class="bg-gradient-to-r from-yellow-500 to-yellow-600 rounded-2xl p-8 mb-8 text-center">
                <h3 class="text-2xl font-bold text-gray-900 mb-4">Ready to Transform Your Home?</h3>
                <p class="text-gray-800 mb-6 max-w-2xl mx-auto">
                    Get your free consultation today and discover how Lion Windows and Doors can enhance your home's beauty, security, and energy efficiency.
                </p>
                <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
                    <a href="tel:+12898036671" class="bg-gray-900 text-white px-8 py-3 rounded-lg font-semibold hover:bg-gray-800 transition-colors duration-300 flex items-center">
                        <i class="fas fa-phone mr-2"></i>Call Now: (289) 803-6671
                    </a>
                    <div class="text-gray-800 font-semibold">
                        <i class="fas fa-clock mr-2"></i>Free Estimates • Licensed & Insured
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <!-- Bottom Footer -->
    <div class="border-t border-gray-700 py-6">
        <div class="container mx-auto px-4">
            <div class="flex flex-col md:flex-row justify-between items-center">
                <div class="text-gray-400 text-sm mb-4 md:mb-0">
                    © 2025 Lion Windows and Doors. All rights reserved. | Licensed & Insured
                </div>
                <div class="flex flex-wrap gap-6 text-sm">
                    <a href="#" class="text-gray-400 hover:text-yellow-500 transition-colors duration-300">Privacy Policy</a>
                    <a href="#" class="text-gray-400 hover:text-yellow-500 transition-colors duration-300">Terms of Service</a>
                    <a href="#" class="text-gray-400 hover:text-yellow-500 transition-colors duration-300">Warranty</a>
                    <a href="#" class="text-gray-400 hover:text-yellow-500 transition-colors duration-300">Careers</a>
                </div>
            </div>
        </div>
    </div>
    
    <!-- Floating Back to Top Button -->
    <button id="backToTop" class="fixed bottom-8 right-8 bg-yellow-500 text-gray-900 w-12 h-12 rounded-full shadow-lg hover:bg-yellow-400 transition-all duration-300 opacity-0 invisible z-50">
        <i class="fas fa-chevron-up"></i>
    </button>
</footer>
'''

FOOTER_JAVASCRIPT = '''
<script>
    // Back to top functionality
    const backToTopBtn = document.getElementById('backToTop');
    
    function toggleBackToTop() {
        if (window.pageYOffset > 300) {
            backToTopBtn.classList.remove('opacity-0', 'invisible');
            backToTopBtn.classList.add('opacity-100', 'visible');
        } else {
            backToTopBtn.classList.add('opacity-0', 'invisible');
            backToTopBtn.classList.remove('opacity-100', 'visible');
        }
    }

    function scrollToTop() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }

    // Event listeners
    window.addEventListener('scroll', toggleBackToTop);
    backToTopBtn.addEventListener('click', scrollToTop);

    // Smooth scrolling for footer links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // SMS Form submission (if form exists)
    const smsForm = document.getElementById("smsForm");
    if (smsForm) {
        smsForm.addEventListener("submit", async (e) => {
            e.preventDefault();
            const form = e.target;
            const data = {
                name: form.name.value,
                email: form.email.value,
                phone: form.phone.value,
                service: form.service.value
            };

            try {
                const res = await fetch("https://clicksend-worker.aidan-shalish.workers.dev", {
                    method: "POST",
                    headers: {"Content-Type": "application/json"},
                    body: JSON.stringify(data)
                });

                const message = await res.text();
                alert(message);
                form.reset();
            } catch (err) {
                alert("Something went wrong. Please try again later.");
            }
        });
    }
</script>'''

def fix_relative_paths(content, file_path):
    """Fix relative paths in the footer based on the file's location."""
    # Count directory depth
    path_parts = Path(file_path).parts
    depth = len(path_parts) - 2  # Subtract for project root and filename
    
    if depth > 0:
        # Add "../" prefix for each directory level
        prefix = "../" * depth
        
        # Fix service links
        content = re.sub(r'href="services/', f'href="{prefix}services/', content)
        
        # Fix index.html links
        content = re.sub(r'href="index\.html', f'href="{prefix}index.html', content)
    
    return content

def add_footer_to_file(file_path):
    """Add footer and JavaScript to a single HTML file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if this is index.html (already has the footer)
        if file_path.endswith('index.html') and 'lionpro' not in file_path:
            print(f"Skipping {file_path} (main index.html already has footer)")
            return
        
        # Remove existing footer if present
        content = re.sub(r'<!--\s*Footer\s*-->.*?</footer>', '', content, flags=re.DOTALL | re.IGNORECASE)
        
        # Remove existing back to top button if present
        content = re.sub(r'<button[^>]*id="backToTop"[^>]*>.*?</button>', '', content, flags=re.DOTALL)
        
        # Remove existing footer scripts
        content = re.sub(r'<script>.*?(backToTop|toggleBackToTop|scrollToTop|smsForm).*?</script>', '', content, flags=re.DOTALL)
        
        # Find the position to insert footer (before </body>)
        body_end_match = re.search(r'</body>', content, re.IGNORECASE)
        if not body_end_match:
            print(f"Warning: No </body> tag found in {file_path}")
            return
        
        # Fix relative paths in footer content
        footer_content = fix_relative_paths(FOOTER_HTML, file_path)
        
        # Insert footer and JavaScript before </body>
        insert_pos = body_end_match.start()
        new_content = (
            content[:insert_pos] + 
            footer_content + 
            "\n" + 
            FOOTER_JAVASCRIPT + 
            "\n" + 
            content[insert_pos:]
        )
        
        # Write the updated content back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✓ Updated footer in {file_path}")
        
    except Exception as e:
        print(f"✗ Error processing {file_path}: {str(e)}")

def main():
    """Main function to process all HTML files."""
    project_root = Path('/Users/ubuntu/WebstormProjects/lionwindowsanddoors')
    
    # Find all HTML files
    html_files = list(project_root.rglob('*.html'))
    
    print(f"Found {len(html_files)} HTML files to process:")
    for file_path in html_files:
        print(f"  - {file_path}")
    
    print("\nProcessing files...")
    
    # Process each file
    for file_path in html_files:
        add_footer_to_file(str(file_path))
    
    print(f"\n✓ Completed processing {len(html_files)} HTML files!")
    print("\nAll HTML files now have the consistent footer with:")
    print("- Company information and contact details")
    print("- Quick links and service links")
    print("- Service areas")
    print("- Call-to-action section")
    print("- Social media links")
    print("- Back-to-top button with smooth scroll")
    print("- SMS form handling (where applicable)")

if __name__ == "__main__":
    main()

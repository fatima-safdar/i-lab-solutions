import re


class AIAgent:
    def __init__(self):
        pass

    def _has_word(self, msg, words):
        """Whole-word match instead of plain substring match."""
        return any(re.search(rf"\b{re.escape(w)}\b", msg) for w in words)

    def generate_reply(self, user_message):
        msg = user_message.lower().strip()

        # 1. Welcome / Greeting Message
        if self._has_word(msg, ["hello", "hi", "hlo", "assalam", "hey", "aoa", "greetings"]):
            return (
                "Hello! Welcome to i-Labsolution AI Agent Support.\n"
                "We take care of your business and your future.\n\n"
                "How can we assist you today? Please choose an option by replying with its number:\n\n"
                "1️⃣ Our IT & Digital Services\n"
                "2️⃣ Professional IT Courses (Admissions Open)\n"
                "3️⃣ Internship Opportunities\n"
                "4️⃣ Social Media Links & Contact Info\n"
                "5️⃣ Our Office Location\n"
                "6️⃣ Office Timings"
            )

        # 2. IT & Digital Services
        elif self._has_word(msg, ["service", "services", "website", "app", "software", "seo"]) or msg == "1":
            return (
                "<strong>Our Professional IT & Digital Services</strong>\n\n"
                "• Website & WordPress Development\n"
                "• Mobile App Development (Android & iOS)\n"
                "• Search Engine Optimization (SEO)\n"
                "• Digital & Social Media Marketing\n"
                "• UI/UX & Graphic Design\n"
                "• E-Commerce Development\n"
                "• Business Software & Automation Solutions\n"
                "• ERP & Campus Management Systems\n"
                "• IT Support & Consultancy\n"
                "• Academic & Final Year Project Assistance\n\n"
                "<strong>Official Website:</strong> <a href='https://i-labsolutions.com' target='_blank'>i-labsolutions.com</a>"
            )

        # 3. IT Courses & Admissions
        elif self._has_word(msg, ["course", "courses", "admission", "learn", "fees"]) or msg == "2":
            return (
                "<strong>Admissions Open – Professional IT Courses</strong>\n"
                "Build your skills and start your journey from learning to earning.\n\n"
                "• Cyber Security\n"
                "• SEO & Digital Marketing\n"
                "• Web Development\n"
                "• Freelancing with Fiverr Expertise\n"
                "• E-Commerce\n"
                "• Flutter Development\n"
                "• CCNA\n\n"
                "<strong>Technical Courses Info:</strong> <a href='https://i-labsolutions.com/technical-courses/' target='_blank'>Click Here</a>\n\n"
                "<strong>Apply for Course Admission:</strong> <a href='https://docs.google.com/forms/d/e/1FAIpQLScRRJhGWxd0rskFq0iMcdGztO0yzP7B3gm0kdyrM5rZr924Xw/viewform?usp=dialog' target='_blank'>Open Admission Form</a>"
            )

        # 4. Internships
        elif self._has_word(msg, ["internship", "internships", "job", "jobs", "work"]) or msg == "3":
            return (
                "<strong>Internship Opportunities Available</strong>\n"
                "Gain practical experience, work on live projects, and kickstart your career.\n\n"
                "<strong>Available Internship Programs:</strong>\n"
                "• Web Development\n"
                "• WordPress Development\n"
                "• Digital Marketing\n"
                "• E-Commerce\n\n"
                "<strong>Apply for Internship:</strong> <a href='https://docs.google.com/forms/d/1dJmF0fvbm57ZqxTbSIPGsLuyi9e--CMI-D6ZrzTXtj4/edit' target='_blank'>Open Internship Form</a>"
            )

        # 5. Social Media & Contact Info
        elif self._has_word(msg, ["contact", "social", "facebook", "youtube", "link", "number", "email"]) or msg == "4":
            return (
                "<strong>Connect With i-Labsolution</strong>\n\n"
                "<strong>Facebook:</strong> <a href='https://www.facebook.com/ilabssolution' target='_blank'>Visit Page</a>\n"
                "<strong>YouTube:</strong> <a href='https://www.youtube.com/@i-LabSolutions' target='_blank'>Watch Channel</a>\n"
                "<strong>TikTok:</strong> <a href='https://www.tiktok.com/@ilabsolutions' target='_blank'>Follow TikTok</a>\n"
                "<strong>Instagram:</strong> <a href='https://www.instagram.com/ilabsolutions' target='_blank'>Follow Instagram</a>\n"
                "<strong>LinkedIn:</strong> <a href='https://www.linkedin.com/company/i-labsolution/' target='_blank'>Connect on LinkedIn</a>\n"
                "<strong>Pinterest:</strong> <a href='https://www.pinterest.com/ilabsolutions/' target='_blank'>View Pinterest</a>\n"
                "<strong>WhatsApp:</strong> <a href='https://wa.me/message/NCZF3WZVGKPIE1' target='_blank'>Chat on WhatsApp</a>\n\n"
                "<strong>Email:</strong> <a href='mailto:info@i-labsolution.com'>info@i-labsolution.com</a>"
            )

        # 6. Location
        elif self._has_word(msg, ["location", "address", "office", "map", "where", "sahiwal"]) or msg == "5":
            return (
                "<strong>i-Labsolution Office Location</strong>\n\n"
                "<strong>Address:</strong> Sahiwal, Punjab, Pakistan.\n\n"
                "<strong>Google Maps:</strong> <a href='https://www.google.com/maps/search/?api=1&query=i-Labsolution+Sahiwal' target='_blank'>Open Map Location</a>"
            )

        # 7. Timings
        elif self._has_word(msg, ["timing", "timings", "time", "open", "close"]) or msg == "6":
            return (
                "<strong>i-Labsolution Office Timings</strong>\n"
                "We are open 7 days a week to support your business goals.\n\n"
                "<strong>Monday to Sunday:</strong> 09:00 AM – 06:00 PM"
            )

        # Default Fallback
        else:
            return (
                "To find more information about i-Labsolution, please choose an option from our menu:\n\n"
                "1️⃣ Services | 2️⃣ Courses | 3️⃣ Internships | 4️⃣ Contact Info | 5️⃣ Location | 6️⃣ Timings\n\n"
                "Or get in touch directly via email at <a href='mailto:info@i-labsolution.com'>info@i-labsolution.com</a>."
            )
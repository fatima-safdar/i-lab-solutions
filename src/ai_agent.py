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
                "Hello! Welcome to i-Lab Solutions AI Agent Support.\n"
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
                "*Our Professional IT & Digital Services*\n\n"
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
                "*Official Website:* https://i-labsolutions.com"
            )

        # 3. IT Courses & Admissions
        elif self._has_word(msg, ["course", "courses", "admission", "learn", "fees"]) or msg == "2":
            return (
                "*Admissions Open – Professional IT Courses*\n"
                "Build your skills and start your journey from learning to earning.\n\n"
                "• Cyber Security\n"
                "• SEO & Digital Marketing\n"
                "• Web Development\n"
                "• Freelancing with Fiverr Expertise\n"
                "• E-Commerce\n"
                "• Flutter Development\n"
                "• CCNA\n\n"
                "*Technical Courses Info:* https://i-labsolutions.com/technical-courses/\n\n"
                "*Apply for Course Admission:* https://docs.google.com/forms/d/e/1FAIpQLScRRJhGWxd0rskFq0iMcdGztO0yzP7B3gm0kdyrM5rZr924Xw/viewform?usp=dialog"
            )

        # 4. Internships
        elif self._has_word(msg, ["internship", "internships", "job", "jobs", "work"]) or msg == "3":
            return (
                "*Internship Opportunities Available*\n"
                "Gain practical experience, work on live projects, and kickstart your career.\n\n"
                "*Available Internship Programs:*\n"
                "• Web Development\n"
                "• WordPress Development\n"
                "• Digital Marketing\n"
                "• E-Commerce\n\n"
                "*Apply for Internship:* https://docs.google.com/forms/d/1dJmF0fvbm57ZqxTbSIPGsLuyi9e--CMI-D6ZrzTXtj4/edit"
            )

        # 5. Social Media & Contact Info
        elif self._has_word(msg, ["contact", "social", "facebook", "youtube", "link", "number", "email"]) or msg == "4":
            return (
                "*Connect With i-Lab Solutions*\n\n"
                "*Facebook:* https://www.facebook.com/ilabssolution\n"
                "*YouTube:* https://www.youtube.com/@i-LabSolutions\n"
                "*TikTok:* https://www.tiktok.com/@ilabsolutions\n"
                "*Instagram:* https://www.instagram.com/ilabsolutions\n"
                "*LinkedIn:* https://www.linkedin.com/company/i-labsolution/\n"
                "*Pinterest:* https://www.pinterest.com/ilabsolutions/\n"
                "*WhatsApp:* https://wa.me/message/NCZF3WZVGKPIE1\n\n"
                "*Email:* info@i-labsolution.com"
            )

        # 6. Location
        elif self._has_word(msg, ["location", "address", "office", "map", "where", "sahiwal"]) or msg == "5":
            return (
                "*i-Lab Solutions Office Location*\n\n"
                "*Address:* Sahiwal, Punjab, Pakistan.\n\n"
                "*Google Maps:* https://www.google.com/maps/search/?api=1&query=i-Labsolution+Sahiwal"
            )

        # 7. Timings
        elif self._has_word(msg, ["timing", "timings", "time", "open", "close"]) or msg == "6":
            return (
                "*i-Lab Solutions Office Timings*\n"
                "We are open 7 days a week to support your business goals.\n\n"
                "*Monday to Sunday:* 09:00 AM – 06:00 PM"
            )

        # Default Fallback
        else:
            return (
                "To find more information about i-Lab Solutions, please choose an option from our menu:\n\n"
                "1️⃣ Services | 2️⃣ Courses | 3️⃣ Internships | 4️⃣ Contact Info | 5️⃣ Location | 6️⃣ Timings\n\n"
                "Or get in touch directly via email at info@i-labsolution.com."
            )

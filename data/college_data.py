"""
Rathinam College Knowledge Base — Scrubbed & Optimized Version
Added keywords for improved search matching (UG, PG, Fees, etc.)
"""

KNOWLEDGE_BASE = [
    # ── ABOUT ──────────────────────────────────────────────────────────────
    {
        "id": "about_1",
        "category": "about",
        "title": "About Rathinam College",
        "keywords": ["about", "history", "vision", "mission", "established", "founded", "rathinam", "college"],
        "content": (
            "Rathinam College is a premier institution located in Coimbatore, "
            "Tamil Nadu, India. Founded in 1997. The college is known for its strong focus on academics, "
            "innovation, and industry-aligned education. The campus spans over 25 acres and offers "
            "state-of-the-art infrastructure including smart classrooms, modern labs, a central library, "
            "sports facilities, and on-campus hostels for boys and girls."
        ),
    },
    {
        "id": "about_2",
        "category": "about",
        "title": "Vision and Mission",
        "keywords": ["vision", "mission", "goal", "objective", "aim", "value"],
        "content": (
            "Vision: To be a world-class institution that nurtures globally competent, ethically "
            "grounded, and socially responsible professionals. "
            "Mission: To provide quality education through innovation, research, and industry "
            "collaboration, empowering students to excel in their chosen fields and contribute "
            "meaningfully to society."
        ),
    },
    # ── COURSES ────────────────────────────────────────────────────────────
    {
        "id": "courses_ug_1",
        "category": "courses",
        "title": "UG Engineering Programs",
        "keywords": ["ug", "u.g", "undergraduate", "bachelor", "degree", "engg", "engineering", "btech", "be", "b.e", "cse", "it", "mech", "ece", "civil", "ai", "ds"],
        "content": (
            "Undergraduate (B.E / B.Tech) programs offered: "
            "1. Computer Science and Engineering (CSE) - 4 years, 60 seats. "
            "2. Information Technology (IT) - 4 years, 60 seats. "
            "3. Electronics and Communication Engineering (ECE) - 4 years, 60 seats. "
            "4. Mechanical Engineering (MECH) - 4 years, 60 seats. "
            "5. Civil Engineering - 4 years, 60 seats. "
            "6. Artificial Intelligence and Data Science (AI&DS) - 4 years, 60 seats. "
            "Eligibility: 10+2 with Physics, Chemistry, and Mathematics (PCM). "
            "Admission is based on merit and specific entrance criteria."
        ),
    },
    {
        "id": "courses_ug_2",
        "category": "courses",
        "title": "UG Arts and Science Programs",
        "keywords": ["ug", "u.g", "undergraduate", "bachelor", "degree", "bsc", "bcom", "bba", "bca", "arts", "science", "commerce"],
        "content": (
            "Undergraduate (B.Sc / B.Com / BBA / BCA) programs: "
            "1. B.Sc Computer Science - 3 years, 60 seats. "
            "2. B.Sc Information Technology - 3 years, 60 seats. "
            "3. B.Com (Computer Applications) - 3 years, 60 seats. "
            "4. BBA (Bachelor of Business Administration) - 3 years, 60 seats. "
            "5. BCA (Bachelor of Computer Applications) - 3 years, 60 seats. "
            "6. B.Sc Mathematics - 3 years, 60 seats. "
            "Eligibility: 10+2 pass in any stream. Direct admission available."
        ),
    },
    {
        "id": "courses_pg_1",
        "category": "courses",
        "title": "Postgraduate Programs",
        "keywords": ["pg", "p.g", "postgraduate", "master", "m.e", "mtech", "mba", "mca", "msc", "management", "higher study"],
        "content": (
            "Postgraduate (M.E / M.Tech / M.Sc / MBA / MCA / M.A / M.Com) programs: "
            "1. M.E Computer Science and Engineering - 2 years. "
            "2. MBA (Master of Business Administration) - 2 years, specialisations in Finance, HR, Marketing, and Operations. "
            "3. MCA (Master of Computer Applications) - 2 years. "
            "4. M.Sc Computer Science - 2 years. "
            "5. M.Sc Data Science - 2 years. "
            "6. M.Sc Biotechnology and M.Sc Applied Psychology - 2 years. "
            "7. M.Com (Master of Commerce) - 2 years. "
            "8. M.A. English Literature and M.A. Journalism - 2 years. "
            "Eligibility: Relevant UG degree. Admission based on entrance scores (TANCET) or merit."
        ),
    },
    {
        "id": "courses_phd",
        "category": "courses",
        "title": "PhD Programs",
        "keywords": ["phd", "p.h.d", "research", "doctoral", "doctorate", "scholar"],
        "content": (
            "Rathinam College offers PhD research programs in the following departments: "
            "Computer Science, Management Studies, Mathematics, Electronics, and English. "
            "Duration: 3 to 5 years. Candidates must qualify in specific entrance exams or hold a "
            "postgraduate degree with 55% marks. Research scholars have access to funded projects, "
            "publication support, and conference grants."
        ),
    },
    # ── ADMISSIONS ─────────────────────────────────────────────────────────
    {
        "id": "admissions_1",
        "category": "admissions",
        "title": "Admission Process and Eligibility",
        "keywords": ["admission", "apply", "eligibility", "process", "portal", "application", "form"],
        "content": (
            "Engineering admissions (B.E/B.Tech): Based on counselling conducted by the state government. "
            "Management quota seats are available directly. "
            "Arts & Science admissions: Direct applications through the college admission portal or in-person. "
            "PG admissions: Based on specific entrance scores like TANCET or merit. "
            "Documents required: marksheets, Transfer Certificate (TC), Community Certificate, "
            "Aadhaar card, and photos. Application fees apply."
        ),
    },
    {
        "id": "admissions_2",
        "category": "admissions",
        "title": "Fee Structure",
        "keywords": ["fee", "fees", "cost", "scholarship", "concession", "payment", "tuition", "hostel fee"],
        "content": (
            "Approximate annual fee structure (2026-27): "
            "B.E / B.Tech: Rs. 155,000 – Rs. 180,000 per year. "
            "B.Sc / BCA / BBA / B.Com: Rs. 98,000 – Rs. 135,000 per year. "
            "MBA: Rs. 255,000 per year. "
            "MCA: Rs. 240,000 per year. "
            "M.Sc: Rs. 120,000 – Rs. 130,000 per year. "
            "Scholarships available: Government scholarships, merit-based fee waivers, and sports quota."
        ),
    },
    # ── DEPARTMENTS & FACULTY ──────────────────────────────────────────────
    {
        "id": "dept_cse",
        "category": "departments",
        "title": "Department of Computer Science and Engineering",
        "keywords": ["cse", "computer", "engineering", "hod", "faculty", "staff", "lab", "it"],
        "content": (
            "The CSE department is one of the largest and most well-equipped departments at Rathinam College. "
            "It has 15 faculty members including several PhD holders. Labs include: Cloud Computing Lab, AI & ML Lab, "
            "Networking Lab, and Software Development Lab. The department runs active student clubs: "
            "Coding Club, Cybersecurity Club, and Hackathon team. "
            "Notable achievements: Students placed in top companies like TCS, Infosys, Wipro, Zoho, and Cognizant."
        ),
    },
    {
        "id": "dept_mech",
        "category": "departments",
        "title": "Department of Mechanical Engineering",
        "keywords": ["mech", "mechanical", "engineering", "hod", "faculty", "lab"],
        "content": (
            "The Mechanical Engineering department offers a strong blend of theoretical and practical education. "
            "Labs: CAD/CAM Lab, Thermal Engineering Lab, Fluid Mechanics Lab, Manufacturing Lab. "
            "Industry collaborations facilitate internships and placements for students."
        ),
    },
    {
        "id": "dept_mba",
        "category": "departments",
        "title": "Department of Management Studies (MBA)",
        "keywords": ["mba", "management", "business", "administration", "hod", "faculty"],
        "content": (
            "The MBA department prepares future business leaders with an industry-integrated curriculum. "
            "Specialisations: Finance, Human Resource Management, Marketing, Operations Management. "
            "Facilities: Seminar Hall, Business Lab, Bloomberg Terminal access. "
            "Placement partners include HDFC Bank, Deloitte, Amazon, and HCL."
        ),
    },
    # ── CAMPUS LIFE & FACILITIES ───────────────────────────────────────────
    {
        "id": "campus_1",
        "category": "campus",
        "title": "Campus Facilities",
        "keywords": ["campus", "hostel", "library", "sports", "gym", "medical", "bus", "transport", "facility", "cafeteria", "mess"],
        "content": (
            "Rathinam College campus facilities include: "
            "Central Library with 50,000+ books and e-journal access. "
            "Sports complex with cricket ground, basketball court, volleyball court, and indoor gym. "
            "Separate hostels for boys and girls with security, Wi-Fi, and mess facility. "
            "Medical centre, cafeteria, food court, and transport facilities covering major routes city-wide."
        ),
    },
    {
        "id": "campus_2",
        "category": "campus",
        "title": "Student Clubs and Activities",
        "keywords": ["club", "nss", "ncc", "rotaract", "ecell", "cultural", "fest", "symposium"],
        "content": (
            "Active student organisations at Rathinam College: "
            "1. NSS – community service activities. "
            "2. NCC – Army and Air Wing. "
            "3. Rotaract Club – social service and leadership. "
            "4. Entrepreneurship Cell – startup incubation support. "
            "5. Cultural Club – annual college fest 'Rathinam Utsav'. "
            "6. Sports Club – inter-collegiate tournaments. "
            "7. Technical Club – hackathons and tech symposiums."
        ),
    },
    # ── EVENTS ─────────────────────────────────────────────────────────────
    {
        "id": "events_1",
        "category": "events",
        "title": "Annual Events and Festivals",
        "keywords": ["event", "fest", "festival", "utsav", "symposium", "graduatation", "freshers"],
        "content": (
            "Key annual events at Rathinam College: "
            "1. Rathinam Utsav (Cultural Fest) – Music, dance, drama, and art competitions. "
            "2. TechRath (Technical Symposium) – Paper presentations, project expo, and workshops. "
            "3. Sports Day – Annual sports meet featuring track & field and team sports. "
            "4. Graduation Day – For final year students. "
            "5. Freshers' Day – Welcome event for new students."
        ),
    },
    # ── PLACEMENTS ─────────────────────────────────────────────────────────
    {
        "id": "placements_1",
        "category": "placements",
        "title": "Placement Cell and Statistics",
        "keywords": ["placement", "job", "career", "salary", "package", "recruit", "company", "interview", "hire", "tcs", "infosys", "wipro", "zoho"],
        "content": (
            "The Rathinam College Placement Cell facilitates campus recruitment for final year students. "
            "Placement highlights: "
            "- Hundreds of students placed across UG and PG programs. "
            "- Top recruiters include TCS, Infosys, Wipro, Cognizant, HCL, Zoho, HDFC Bank, Deloitte, Amazon, and L&T. "
            "Placement support services: resume building workshops, mock interviews, aptitude training, "
            "and soft skills development."
        ),
    },
]

import random
import pandas as pd
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="TalentGrid AI — Autonomous HRMS & Analytics Portal",
    page_icon="⚡",
    layout="wide",
)

# -------------------------------------------------------------
# 1. LOGIN & LOGOUT SYSTEM
# -------------------------------------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 TalentGrid AI — HRMS Portal Login")
    st.markdown(
        "Please enter your administrator credentials to access the 500+ Employee Directory Portal."
    )

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_btn = st.form_submit_button("Login to Portal")

        if login_btn:
            if username == "admin" and password == "admin123":
                st.session_state.logged_in = True
                st.toast("✅ Logged in successfully!", icon="🔓")
                st.rerun()
            else:
                st.error(
                    "Invalid Username or Password. (Default: admin / admin123)"
                )
    st.stop()

# -------------------------------------------------------------
# 2. CONSTANTS & DATA GENERATION
# -------------------------------------------------------------
FIRST_NAMES = [
    "Ali",
    "Ahmed",
    "Usman",
    "Hamza",
    "Bilal",
    "Tariq",
    "Omer",
    "Zaid",
    "Fatima",
    "Ayesha",
    "Zainab",
    "Sana",
    "Maryam",
    "Hira",
    "Sadia",
    "Kashif",
    "Farhan",
    "Saad",
    "Asad",
    "Noman",
    "Shazia",
    "Rabia",
    "Mehwish",
    "Faisal",
    "Kamran",
    "Shahid",
    "Imran",
    "Yasir",
    "Saba",
    "Mahnoor",
]

LAST_NAMES = [
    "Khan",
    "Sheikh",
    "Siddiqui",
    "Raza",
    "Malik",
    "Chaudhry",
    "Ahmed",
    "Hassan",
    "Qureshi",
    "Mughal",
    "Bhatti",
    "Shah",
    "Mirza",
    "Iqbal",
    "Farooqui",
]

PAKISTAN_CITIES = [
    "Karachi, Pakistan",
    "Lahore, Pakistan",
    "Islamabad, Pakistan",
    "Rawalpindi, Pakistan",
    "Faisalabad, Pakistan",
    "Multan, Pakistan",
    "Peshawar, Pakistan",
    "Quetta, Pakistan",
    "Sialkot, Pakistan",
    "Hyderabad, Pakistan",
    "Gujranwala, Pakistan",
    "Sukkur, Pakistan",
    "Mianwali, Pakistan",
]

DEPARTMENTS = [
    "Engineering",
    "Sales & Marketing",
    "Human Resources",
    "Finance",
    "Operations",
    "Quality Assurance",
    "Supply Chain",
    "Research & Development",
]

EMPLOYMENT_TYPES = ["Full-Time", "Contract", "Executive"]
RECRUITMENT_SOURCES = [
    "LinkedIn",
    "Indeed",
    "Company Career Portal",
    "Employee Referral",
    "Walk-In",
    "Facebook",
    "Glassdoor",
]


def generate_500_data():
    random.seed(42)
    records = []
    for i in range(1, 501):
        emp_id = f"EMP-{1000 + i}"
        name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"

        city = random.choices(
            PAKISTAN_CITIES,
            weights=[30, 25, 10, 8, 6, 5, 4, 3, 3, 2, 2, 1, 1],
            k=1,
        )[0]
        dept = random.choice(DEPARTMENTS)
        emp_type = random.choices(
            EMPLOYMENT_TYPES, weights=[75, 20, 5], k=1
        )[0]

        if emp_type == "Executive":
            salary = random.randint(700000, 1500000)
            std_shift = 8
            avg_hours = round(random.uniform(8.5, 12.0), 1)
        elif emp_type == "Full-Time":
            salary = random.randint(180000, 650000)
            std_shift = random.choice([8, 12])
            avg_hours = round(random.uniform(8.0, 13.5), 1)
        else:
            salary = random.randint(80000, 170000)
            std_shift = random.choice([8, 12])
            avg_hours = round(random.uniform(7.5, 11.0), 1)

        days_present = random.randint(22, 30)
        paid_leaves = random.randint(0, 3)
        unpaid_leaves = (
            random.choices([0, 1, 2, 3, 4], weights=[80, 10, 5, 3, 2], k=1)[0]
        )
        perf_rating = round(random.uniform(2.8, 5.0), 1)

        records.append(
            {
                "Employee_ID": emp_id,
                "Name": name,
                "Region": city,
                "Department": dept,
                "Employment_Type": emp_type,
                "Base_Monthly_Salary_PKR": salary,
                "Total_Working_Days": 30,
                "Days_Present": days_present,
                "Paid_Leaves": paid_leaves,
                "Unpaid_Leaves": unpaid_leaves,
                "Standard_Shift_Hours": std_shift,
                "Avg_Daily_Working_Hours": avg_hours,
                "Performance_Rating": perf_rating,
            }
        )

    return pd.DataFrame(records)


def generate_candidate_data():
    random.seed(101)
    candidates = []
    positions = [
        "Software Engineer",
        "HR Manager",
        "Sales Executive",
        "Financial Analyst",
        "Supply Chain Officer",
        "QA Specialist",
    ]
    statuses = ["Hired", "Interviewing", "Applied", "Rejected"]

    for i in range(1, 21):
        f_name = random.choice(FIRST_NAMES)
        l_name = random.choice(LAST_NAMES)
        full_name = f"{f_name} {l_name}"
        father_name = f"{random.choice(FIRST_NAMES)} {l_name}"
        cnic = f"42101-{random.randint(1000000, 9999999)}-{random.randint(1, 9)}"
        contact = f"03{random.randint(0, 4)}{random.randint(10000000, 99999999)}"
        city = random.choice(PAKISTAN_CITIES)
        address = (
            f"House #{random.randint(1, 150)}, Street {random.randint(1, 20)}, {city.split(',')[0]}"
        )
        designation = random.choice(positions)
        source = random.choice(RECRUITMENT_SOURCES)
        status = random.choice(statuses)

        candidates.append(
            {
                "Application_ID": f"APP-{5000 + i}",
                "Full_Name": full_name,
                "Father_Name": father_name,
                "CNIC": cnic,
                "Contact_No": contact,
                "City": city,
                "Address": address,
                "Designation": designation,
                "Recruitment_Source": source,
                "Status": status,
            }
        )
    return pd.DataFrame(candidates)


if "df_emp" not in st.session_state:
    st.session_state.df_emp = generate_500_data()

if "df_candidates" not in st.session_state:
    st.session_state.df_candidates = generate_candidate_data()

# -------------------------------------------------------------
# 3. SIDEBAR NAVIGATION & GLOBAL FILTERS
# -------------------------------------------------------------
st.sidebar.title("⚡ TalentGrid AI")

if st.sidebar.button("🔴 Logout"):
    st.session_state.logged_in = False
    st.toast("Logged out successfully!", icon="🔒")
    st.rerun()

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation Menu",
    [
        "📊 Executive Dashboard & Cost Analytics",
        "⏱️ Attendance & Payroll Register",
        "📄 Pay Slip Generator",
        "🤖 Workforce Insights & Attrition Analysis",
        "🚨 Autonomous HR Risk Prevention Center",
        "📋 Candidate Application & Onboarding Record",
        "📝 Global Data Entry Form",
        "📁 Directory & Export (500 Records)",
    ],
)

st.sidebar.markdown("---")
st.sidebar.subheader("🌐 Global Filters")

all_cities = ["All Cities"] + sorted(
    list(st.session_state.df_emp["Region"].unique())
)
selected_city = st.sidebar.selectbox("Office / City Location", all_cities)

all_depts = ["All Departments"] + sorted(
    list(st.session_state.df_emp["Department"].unique())
)
selected_dept = st.sidebar.selectbox("Department", all_depts)

all_types = ["All Types"] + sorted(
    list(st.session_state.df_emp["Employment_Type"].unique())
)
selected_type = st.sidebar.selectbox("Employment Status", all_types)

df_filtered = st.session_state.df_emp.copy()

if selected_city != "All Cities":
    df_filtered = df_filtered[df_filtered["Region"] == selected_city]

if selected_dept != "All Departments":
    df_filtered = df_filtered[df_filtered["Department"] == selected_dept]

if selected_type != "All Types":
    df_filtered = df_filtered[
        df_filtered["Employment_Type"] == selected_type
    ]

target_budget = 200000000
total_payroll = int(df_filtered["Base_Monthly_Salary_PKR"].sum())

if total_payroll <= target_budget:
    st.success(
        f"✅ Budget Safe: Filtered Payroll (Rs. {total_payroll:,}) is balanced within allocation (Rs. {target_budget:,})."
    )
else:
    st.error(
        f"⚠️ Budget Warning: Filtered Payroll (Rs. {total_payroll:,}) exceeds budget (Rs. {target_budget:,})."
    )

# -------------------------------------------------------------
# PAGE 1: EXECUTIVE DASHBOARD
# -------------------------------------------------------------
if page == "📊 Executive Dashboard & Cost Analytics":
    st.title("📊 Executive Summary & Cost Analytics")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Filtered Headcount", f"{len(df_filtered)} / 500")
    c2.metric("Allocated Budget", f"Rs. {target_budget:,}")
    c3.metric("Total Net Payroll", f"Rs. {total_payroll:,}")
    avg_sal = int(total_payroll / len(df_filtered)) if len(df_filtered) > 0 else 0
    c4.metric("Avg. Monthly Compensation", f"Rs. {avg_sal:,}")

    st.markdown("---")
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("Departmental Payroll Cost (PKR)")
        dept_cost = (
            df_filtered.groupby("Department")["Base_Monthly_Salary_PKR"]
            .sum()
            .reset_index()
        )
        st.bar_chart(
            dept_cost.set_index("Department"), use_container_width=True
        )

    with col_right:
        st.subheader("City-wise Workforce Distribution")
        city_count = (
            df_filtered.groupby("Region")["Employee_ID"].count().reset_index()
        )
        city_count.columns = ["City / Region", "Employee Count"]
        st.dataframe(city_count, use_container_width=True)

# -------------------------------------------------------------
# PAGE 2: ATTENDANCE & PAYROLL REGISTER
# -------------------------------------------------------------
elif page == "⏱️ Attendance & Payroll Register":
    st.title("⏱️ Attendance, Shift Timings & Payroll Register")
    st.markdown(
        f"Showing **{len(df_filtered)}** employee records based on active filters."
    )

    st.dataframe(
        df_filtered[
            [
                "Employee_ID",
                "Name",
                "Region",
                "Department",
                "Standard_Shift_Hours",
                "Avg_Daily_Working_Hours",
                "Days_Present",
                "Paid_Leaves",
                "Unpaid_Leaves",
                "Base_Monthly_Salary_PKR",
            ]
        ],
        use_container_width=True,
    )

# -------------------------------------------------------------
# PAGE 3: PAY SLIP GENERATOR
# -------------------------------------------------------------
elif page == "📄 Pay Slip Generator":
    st.title("📄 Official Automated Pay Slip Generator")

    if len(df_filtered) == 0:
        st.info("No employees match the current filter selection.")
    else:
        emp_list = df_filtered["Employee_ID"] + " - " + df_filtered["Name"]
        selected_option = st.selectbox("Select Employee", emp_list)
        selected_emp_id = selected_option.split(" - ")[0]
        selected_emp = df_filtered[
            df_filtered["Employee_ID"] == selected_emp_id
        ].iloc[0]

        st.markdown("---")

        st.markdown(
            f"""
            <div style="background-color: #ffffff; padding: 25px; border-radius: 12px; border: 1px solid #e5e7eb; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);">
                <h3 style="color: #059669; margin-top: 0;">⚡ TalentGrid AI — Official Salary Slip</h3>
                <hr style="border-top: 1px solid #e5e7eb;">
                <p style="color: #374151; font-size: 15px;"><strong>Employee Name:</strong> {selected_emp['Name']} &nbsp;|&nbsp; <strong>Employee ID:</strong> {selected_emp['Employee_ID']}</p>
                <p style="color: #374151; font-size: 15px;"><strong>Department:</strong> {selected_emp['Department']} &nbsp;|&nbsp; <strong>Office Region:</strong> {selected_emp['Region']}</p>
                <p style="color: #374151; font-size: 15px;"><strong>Shift Requirement:</strong> {selected_emp['Standard_Shift_Hours']} Hours/Day &nbsp;|&nbsp; <strong>Avg Worked:</strong> {selected_emp['Avg_Daily_Working_Hours']} Hrs/Day</p>
                <hr style="border-top: 1px solid #e5e7eb;">
                <p style="color: #1f2937; font-size: 18px;"><strong>Base Monthly Salary:</strong> Rs. {selected_emp['Base_Monthly_Salary_PKR']:,}</p>
                <p style="color: #059669; font-weight: bold;">Company Performance Increment Applied: 15%</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# -------------------------------------------------------------
# PAGE 4: WORKFORCE INSIGHTS
# -------------------------------------------------------------
elif page == "🤖 Workforce Insights & Attrition Analysis":
    st.title("🧠 AI Workforce Intelligence & Attrition Analytics")

    c1, c2 = st.columns(2)

    with c1:
        st.subheader("Attrition Risk & Unpaid Leaves")
        risk_df = df_filtered[df_filtered["Unpaid_Leaves"] >= 2]
        st.warning(
            f"Identified {len(risk_df)} employees with high unpaid leaves."
        )
        st.dataframe(
            risk_df[
                [
                    "Employee_ID",
                    "Name",
                    "Region",
                    "Department",
                    "Unpaid_Leaves",
                    "Performance_Rating",
                ]
            ],
            use_container_width=True,
        )

    with c2:
        st.subheader("Top Performers (Rating >= 4.5)")
        top_df = df_filtered[df_filtered["Performance_Rating"] >= 4.5]
        st.dataframe(
            top_df[
                [
                    "Employee_ID",
                    "Name",
                    "Region",
                    "Department",
                    "Performance_Rating",
                ]
            ],
            use_container_width=True,
        )

# -------------------------------------------------------------
# PAGE 5: AUTONOMOUS HR RISK PREVENTION CENTER
# -------------------------------------------------------------
elif page == "🚨 Autonomous HR Risk Prevention Center":
    st.title(
        "🚨 Autonomous HR Risk Prevention Center (5 World-First Features)"
    )
    st.markdown(
        "Automated background systems scanning for payroll leaks, ghosting risks, burnout hazards, and salary disparities."
    )

    col_a, col_b = st.columns(2)

    with col_a:
        st.subheader("1️⃣ Ghosting & Sudden Exit Hazard")
        ghost_df = df_filtered[df_filtered["Unpaid_Leaves"] >= 2]
        st.error(
            f"High Risk Alert: {len(ghost_df)} staff member(s) at ghosting/exit risk."
        )
        st.dataframe(
            ghost_df[["Employee_ID", "Name", "Region", "Unpaid_Leaves"]],
            use_container_width=True,
        )
        if st.button("Email Ghosting Risk Alert"):
            st.toast("Ghosting alert dispatched!", icon="🚨")

    with col_b:
        st.subheader("2️⃣ Salary Disparity & Poaching Hazard")
        poach_df = df_filtered[df_filtered["Performance_Rating"] >= 4.5]
        st.warning(
            f"Identified {len(poach_df)} Top-Performer(s) with retention review notice."
        )
        st.dataframe(
            poach_df[
                [
                    "Employee_ID",
                    "Name",
                    "Department",
                    "Performance_Rating",
                    "Base_Monthly_Salary_PKR",
                ]
            ],
            use_container_width=True,
        )
        if st.button("Email Compensation Review"):
            st.toast("Compensation review email dispatched!", icon="💼")

    st.markdown("---")
    r1, r2 = st.columns(2)

    with r1:
        st.subheader("3️⃣ Burnout Hazard Predictor")
        burn_df = df_filtered[
            df_filtered["Avg_Daily_Working_Hours"]
            > df_filtered["Standard_Shift_Hours"]
        ]
        st.error(
            f"Burnout Alert: {len(burn_df)} staff working excessive overtime hours."
        )
        st.dataframe(
            burn_df[
                [
                    "Employee_ID",
                    "Name",
                    "Standard_Shift_Hours",
                    "Avg_Daily_Working_Hours",
                ]
            ],
            use_container_width=True,
        )
        if st.button("Dispatch Burnout Warning"):
            st.toast("Burnout warning sent!", icon="⚠️")

    with r2:
        st.subheader("4️⃣ & 5️⃣ Custom Automated Email Gateway")
        with st.form("custom_email_form"):
            subj = st.text_input(
                "Email Subject", value="TalentGrid HR Executive Notice"
            )
            body = st.text_area(
                "Email Content",
                value="Automated notification generated from TalentGrid AI portal.",
            )
            recip = st.text_input(
                "Recipient Email", value="owner@talentgrid.ai"
            )
            send_mail = st.form_submit_button("🚀 Send Direct Email Alert")

            if send_mail:
                st.toast(
                    f"Email sent successfully to {recip}!", icon="📩"
                )
                st.success("Custom Email Gateway Dispatched Successfully!")

# -------------------------------------------------------------
# PAGE 6: CANDIDATE APPLICATION & ONBOARDING RECORD (NEW TAB)
# -------------------------------------------------------------
elif page == "📋 Candidate Application & Onboarding Record":
    st.title("📋 Candidate Application, Recruitment & Onboarding Record")
    st.markdown(
        "Manage candidate application details including personal info, CNIC, contact details, recruitment source, and designation."
    )

    # Sub-tabs: View All Applications / Add New Candidate Form
    tab1, tab2 = st.tabs(
        ["📊 View Candidate Records", "➕ Register New Candidate Application"]
    )

    with tab1:
        st.subheader("Master Candidate Application Directory")

        col_f1, col_f2 = st.columns(2)
        with col_f1:
            source_filter = st.selectbox(
                "Filter by Source",
                ["All Sources"] + RECRUITMENT_SOURCES,
            )
        with col_f2:
            status_filter = st.selectbox(
                "Filter by Status",
                ["All Statuses", "Applied", "Interviewing", "Hired", "Rejected"],
            )

        cand_df = st.session_state.df_candidates.copy()

        if source_filter != "All Sources":
            cand_df = cand_df[cand_df["Recruitment_Source"] == source_filter]

        if status_filter != "All Statuses":
            cand_df = cand_df[cand_df["Status"] == status_filter]

        st.dataframe(cand_df, use_container_width=True)

        # Download Candidate Data
        cand_csv = cand_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download Candidate Applications CSV",
            data=cand_csv,
            file_name="Candidate_Applications_Record.csv",
            mime="text/csv",
        )

    with tab2:
        st.subheader("Candidate Entry & Application Tracking Form")

        with st.form("candidate_registration_form"):
            col_a, col_b = st.columns(2)

            with col_a:
                app_id = f"APP-{5000 + len(st.session_state.df_candidates) + 1}"
                cand_name = st.text_input(
                    "Candidate Full Name*", placeholder="e.g. Tariq Mehmood"
                )
                father_name = st.text_input(
                    "Father's Name*", placeholder="e.g. Mehmood Akhtar"
                )
                cnic_no = st.text_input(
                    "CNIC / NIC Number*", placeholder="e.g. 42101-1234567-1"
                )
                contact_no = st.text_input(
                    "Contact Number*", placeholder="e.g. 0300-1234567"
                )
                city_loc = st.selectbox(
                    "City Location*", PAKISTAN_CITIES, index=0
                )

            with col_b:
                address = st.text_area(
                    "Residential Address*",
                    placeholder="e.g. House #123, Block 4, PECHS, Karachi",
                )
                designation = st.text_input(
                    "Applied Position / Designation*",
                    placeholder="e.g. Senior Software Engineer",
                )
                source = st.selectbox(
                    "Recruitment Source (Where Applied?)*", RECRUITMENT_SOURCES
                )
                app_status = st.selectbox(
                    "Application Status",
                    ["Applied", "Interviewing", "Hired", "Rejected"],
                )

            submit_cand = st.form_submit_button(
                "💾 Save Candidate Application Record"
            )

            if submit_cand:
                if (
                    cand_name.strip() == ""
                    or cnic_no.strip() == ""
                    or contact_no.strip() == ""
                ):
                    st.warning(
                        "Please fill in all mandatory fields (Name, CNIC, and Contact Number)."
                    )
                else:
                    new_candidate = {
                        "Application_ID": app_id,
                        "Full_Name": cand_name,
                        "Father_Name": father_name,
                        "CNIC": cnic_no,
                        "Contact_No": contact_no,
                        "City": city_loc,
                        "Address": address,
                        "Designation": designation,
                        "Recruitment_Source": source,
                        "Status": app_status,
                    }

                    st.session_state.df_candidates = pd.concat(
                        [
                            st.session_state.df_candidates,
                            pd.DataFrame([new_candidate]),
                        ],
                        ignore_index=True,
                    )

                    st.toast(
                        f"✅ Candidate {cand_name} ({app_id}) saved successfully via {source}!",
                        icon="🎉",
                    )
                    st.success(
                        f"Application for {cand_name} ({designation}) registered in candidate database!"
                    )

# -------------------------------------------------------------
# PAGE 7: GLOBAL DATA ENTRY FORM
# -------------------------------------------------------------
elif page == "📝 Global Data Entry Form":
    st.title("📝 Register New Employee Profile")

    with st.form("entry_form"):
        c1, c2 = st.columns(2)
        with c1:
            emp_id = st.text_input(
                "Employee ID", value=f"EMP-{1000 + len(st.session_state.df_emp) + 1}"
            )
            full_name = st.text_input("Full Name", placeholder="e.g. Hassan Raza")
            region = st.selectbox("Office / City Location", PAKISTAN_CITIES)
            base_salary = st.number_input("Base Monthly Salary (PKR)", value=300000)
            std_shift = st.selectbox("Standard Shift Hours", [8, 12])

        with c2:
            dept = st.selectbox("Department", DEPARTMENTS)
            emp_status = st.selectbox("Employment Status", EMPLOYMENT_TYPES)
            avg_hours = st.number_input("Avg Daily Working Hours", value=12.0)
            days_present = st.number_input("Days Present", value=28)
            paid_leaves = st.number_input("Paid Leaves", value=2)
            unpaid_leaves = st.number_input("Unpaid Leaves", value=0)

        submitted = st.form_submit_button("💾 Save & Sync Profile")

        if submitted:
            if full_name.strip() == "":
                st.warning("Please enter employee full name.")
            else:
                new_record = {
                    "Employee_ID": emp_id,
                    "Name": full_name,
                    "Region": region,
                    "Department": dept,
                    "Employment_Type": emp_status,
                    "Base_Monthly_Salary_PKR": base_salary,
                    "Total_Working_Days": 30,
                    "Days_Present": days_present,
                    "Paid_Leaves": paid_leaves,
                    "Unpaid_Leaves": unpaid_leaves,
                    "Standard_Shift_Hours": std_shift,
                    "Avg_Daily_Working_Hours": avg_hours,
                    "Performance_Rating": 4.0,
                }
                st.session_state.df_emp = pd.concat(
                    [st.session_state.df_emp, pd.DataFrame([new_record])],
                    ignore_index=True,
                )

                st.toast(
                    f"✅ Employee {emp_id} ({full_name}) registered successfully!",
                    icon="🎉",
                )
                st.success(
                    f"Profile for {full_name} ({region}) added to 500+ master directory!"
                )

# -------------------------------------------------------------
# PAGE 8: DIRECTORY & EXPORT
# -------------------------------------------------------------
elif page == "📁 Directory & Export (500 Records)":
    st.title("📁 Master Employee Directory & CSV Export")

    search_query = st.text_input("🔍 Live Search Employee (Name or ID)")

    display_df = df_filtered
    if search_query:
        display_df = display_df[
            display_df["Name"]
            .str.contains(search_query, case=False, na=False)
            | display_df["Employee_ID"]
            .str.contains(search_query, case=False, na=False)
        ]

    st.write(f"Displaying **{len(display_df)}** matching employee records:")
    st.dataframe(display_df, use_container_width=True)

    csv_data = display_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Complete Master CSV Record",
        data=csv_data,
        file_name="TalentGrid_AI_500_Employee_Directory.csv",
        mime="text/csv",
    )
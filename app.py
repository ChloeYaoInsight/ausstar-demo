import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Ausstar 临床随访系统 Demo", layout="wide")

st.sidebar.title("Ausstar 数字化质保系统")
menu = st.sidebar.radio("功能导航", ["门诊控制台", "患者全生命周期档案", "新增临床记录", "生成报告预览"])

if menu == "门诊控制台":
    st.title("🏥 门诊业绩与随访工作台 (2026年 8月)")
    st.info("💡 商业展示亮点：将随访转化为复诊率。前台每天打开系统，就知道今天该打给谁、能产生多少潜在业绩。")
    
    # 核心商业看板 (KPI 驱动)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("本月待召回总人数", "24 人", "较上月 +3 人")
    col2.metric("已成功预约复诊", "15 人", "转化率 62.5%")
    col3.metric("剩余待电话沟通", "9 人", "-")
    col4.metric("本月系统消耗质保额度", "12 颗", "Ausstar 植体")
    
    st.markdown("---")
    
    # 按月维度的待预约沟通名单
    st.subheader("📞 本月待电话沟通名单 (行动指令)")
    
    # 模拟带有行动指导意义的数据流
    recall_data = pd.DataFrame({
        "患者姓名": ["李女士 (P-008)", "王先生 (P-012)", "赵阿姨 (P-045)", "陈先生 (P-055)"],
        "联系电话": ["138-xxxx-1122", "139-xxxx-3344", "136-xxxx-5566", "137-xxxx-7788"],
        "触发原因 (系统自动计算)": ["术后3个月：需预约二期取模", "术后半年：常规洗牙与X光复查", "术后1年：种植体周围炎风险排查", "术后即刻：次日电话回访痛感"],
        "上次就诊时间": ["2026-05-15", "2026-02-10", "2025-08-20", "2026-08-18"],
        "沟通状态": ["待拨打", "电话未接", "待拨打", "已预约 (明日10点)"]
    })
    
    # 在 Streamlit 中展示可交互的表格
    st.dataframe(recall_data, use_container_width=True)
    
    st.button("下载本月待沟通名单 (Excel)", type="secondary")
    
    st.markdown("---")
    
    st.subheader("📝 近期已完成的临床动态 (流水账)")
    recent_data = pd.DataFrame({
        "患者编号": ["P-2026-001", "P-2026-002", "P-2026-003"],
        "核心事件": ["完成一期手术 (右下6)", "术前方案确认 (左下4)", "两年期复查 (右上4)"],
        "操作日期": ["2026-08-19", "2026-08-19", "2026-08-18"],
        "操作医生": ["张医生", "李医生", "张医生"]
    })
    st.dataframe(recent_data, use_container_width=True)

elif menu == "患者全生命周期档案":
    st.title("🗂️ 患者全生命周期档案 (按牙位独立建轴)")
    
    search_col1, search_col2 = st.columns([3, 1])
    with search_col1:
        st.text_input("请输入患者编号或手机号检索：", value="P-2026-001 (演示账号)")
    with search_col2:
        st.markdown("<br>", unsafe_allow_html=True) 
        st.button("🔍 搜索档案")
        
    st.markdown("---")
    st.subheader("👤 张先生 | 累计种植体：2 颗")
    
    tab1, tab2 = st.tabs(["🦷 植体 1：右下 6 (最新)", "🦷 植体 2：右上 4 (历史维护)"])
    
    with tab1:
        st.markdown("""
        ### ⏱️ 右下 6 独立时间轴
        > **🟢 [2026年 8月 19日] - 阶段二：一期植入手术** 
        > * ⚙️ **植体溯源**：Ausstar Pro-Active | 批号: AUS-8821 | 生产日期: 2025-11-20
        > * 📝 **临床记录**：ISQ 8.5。
        > * 🦴 **骨粉植入**：Bio-Oss (0.25g)
        > * 🖼️ **影像**：✅ 术后全景片已上传
        """)

    with tab2:
        st.markdown("""
        ### ⏱️ 右上 4 独立时间轴 
        > **🟢 [2026年 5月 10日] - 阶段四：常规复查** 
        > * 📝 **标准化记录**：两年期复查，骨结合完美，无边缘骨吸收。
        """)

elif menu == "新增临床记录":
    st.title("📝 新增临床记录 (全周期标准化录入)")
    
    with st.form("clinical_form"):
        col1, col2 = st.columns(2)
        with col1:
            patient_id = st.text_input("患者编号")
            tooth_position = st.selectbox("选择操作牙位", ["右下 6", "右上 4", "新增牙位..."])
        with col2:
            stage = st.selectbox("当前临床阶段", [
                "1. 术前评估与方案设计", 
                "2. 一期植入手术", 
                "3. 二期修复与戴牙",
                "4. 常规复查与维护"
            ])
            doctor_name = st.text_input("主诊医生姓名", value="张医生")
            
        st.markdown("---")
        
        if "术前" in stage:
            st.subheader("1️⃣ 术前评估与合规文件")
            chief_complaint = st.selectbox("患者主诉", ["单颗牙缺失", "多颗牙缺失", "全口/半口牙缺失", "外伤导致脱落"])
            st.text_area("诊疗方案备注")
            st.info("系统已自动生成标准版《种植手术知情同意书》及相关风险揭示。")
            consent_signed = st.checkbox("✅ 患者本人已阅读并在终端设备上完成电子签名确认")
            
        elif "一期" in stage:
            st.subheader("2️⃣ 一期手术与耗材溯源")
            col3, col4, col5 = st.columns(3)
            with col3:
                implant_model = st.selectbox("Ausstar 植体型号", ["Pro-Active", "Classic", "Mini"])
            with col4:
                implant_batch = st.text_input("植体批号 (支持扫码输入)")
            with col5:
                production_date = st.date_input("植体生产日期", datetime.date(2025, 1, 1))
            
            st.markdown("<br>", unsafe_allow_html=True)
            isq_score = st.slider("初期稳定性 ISQ 评分", 1.0, 100.0, 75.0, step=0.5)
            
            st.markdown("<br>", unsafe_allow_html=True)
            need_bone_graft = st.checkbox("🦴 本次手术是否进行植骨 (GBR/植骨术)？")
            
            if need_bone_graft:
                bone_col1, bone_col2 = st.columns(2)
                with bone_col1:
                    bone_brand = st.selectbox("骨粉品牌", ["Bio-Oss", "Osteon", "国产同种异体骨", "其他"])
                with bone_col2:
                    bone_amount = st.text_input("植入量 (如: 0.25g / 0.5g)")

        elif "二期" in stage:
            st.subheader("3️⃣ 二期修复与加工厂信息")
            col_res1, col_res2 = st.columns(2)
            with col_res1:
                healing_abutment = st.text_input("愈合基台型号")
                restoration_abutment = st.text_input("修复基台型号")
            with col_res2:
                crown_material = st.selectbox("牙冠材质", ["氧化锆全瓷冠", "玻璃陶瓷", "金属烤瓷 (PFM)", "纯钛冠"])
                dental_lab = st.text_input("技工加工厂名称", placeholder="如：精工齿科 / 现代牙科")
                
        elif "常规" in stage:
            st.subheader("4️⃣ 常规复查评估")
            bone_status = st.radio("骨结合效果评估", ["优良（无边缘骨吸收）", "正常（符合预期）", "欠佳（存在吸收）"])
            periodontal_status = st.radio("牙周与软组织状态", ["健康，无红肿", "轻微探诊出血 (BOP+)", "种植体周围炎倾向"])

        st.markdown("---")
        uploaded_file = st.file_uploader("🖼️ 请上传当前阶段影像资料", type=['jpg', 'png', 'jpeg'])
        submitted = st.form_submit_button("保存并同步至时间轴")
        
        if submitted:
            st.success(f"✅ 临床记录保存成功！")

elif menu == "生成报告预览":
    st.title("📱 患者端：终身数字护照 (演示)")
    
    st.markdown("---")
    with st.container():
        st.success("🔔 微信服务通知：张医生为您更新了【Ausstar 终身数字护照】")
        st.markdown("### 🦷 我的口腔种植资产总览")
        st.info("👤 **患者**：张先生 | 🛡️ **当前受保护植体**：2 颗")
        
        with st.expander("🦷 植体 1：右下 6 (最新动态)", expanded=True):
            st.markdown("""
            * **品牌型号**：Ausstar Pro-Active
            * **唯一防伪码**：`AUS-8821` 🟢
            ---
            **时光机 (历史轨迹)**：
            * `[2026-08-19]` 成功完成一期植入手术。状态优良。
            """)

import streamlit as st

st.set_page_config(page_title="죽음을 즐기는 기사", page_icon="⚔️", layout="centered")
st.title("⚔️ 죽음을 즐기는 기사")
st.caption("리벤쳐 스타일 | 웃기고 특이한 죽음이 가득한 어드벤처")

# ==================== 세션 상태 ====================
if "location" not in st.session_state:
    st.session_state.location = "성 앞 광장"
if "knowledge" not in st.session_state:
    st.session_state.knowledge = set()
if "death_count" not in st.session_state:
    st.session_state.death_count = 0
if "death_log" not in st.session_state:
    st.session_state.death_log = []

# ==================== 죽음 처리 ====================
def die(death_message, knowledge_gained=None):
    st.session_state.death_count += 1
    st.session_state.death_log.append(death_message)
    
    if knowledge_gained:
        st.session_state.knowledge.add(knowledge_gained)
    
    st.error(f"💀 {death_message}")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 다시 시작하기", use_container_width=True, key="restart"):
            st.session_state.location = "성 앞 광장"
            st.rerun()
    with col2:
        if st.button("📜 죽음 기록 보기", use_container_width=True, key="log"):
            st.session_state.show_death_log = True
            st.rerun()

# ==================== 상태 표시 ====================
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("죽은 횟수", st.session_state.death_count)
with col2:
    st.metric("알게 된 지식", len(st.session_state.knowledge))
with col3:
    if st.button("📜 죽음 기록"):
        st.session_state.show_death_log = True

if st.session_state.get("show_death_log"):
    with st.expander("💀 지금까지의 죽음 기록", expanded=True):
        if st.session_state.death_log:
            for i, death in enumerate(reversed(st.session_state.death_log[-10:]), 1):
                st.write(f"{i}. {death}")
        else:
            st.write("아직 죽은 적이 없습니다.")
    if st.button("닫기"):
        st.session_state.show_death_log = False
        st.rerun()

st.markdown("---")

# ==================== 현재 장소 ====================
st.subheader(f"📍 현재 위치: {st.session_state.location}")

if st.session_state.location == "성 앞 광장":
    st.write("넓은 성 앞 광장이다. 멀리 울창한 숲이 보이고, 성벽 위에서 병사들이 순찰을 돌고 있다.")
    st.write("기사인 너는 오늘도 새로운 모험을 떠나고 싶다. 그런데 왠지 모르게 불길한 기운이 감돈다.")

    st.markdown("### 무엇을 할까?")

    # === 선택지들 ===
    if st.button("🌲 왼쪽 숲으로 들어간다"):
        st.session_state.location = "숲 입구"
        st.rerun()

    if st.button("🏰 성 안으로 들어간다"):
        die(
            "성 안으로 들어서자마자 경비병이 창을 들고 달려왔다. "
            "'침입자다!'라는 외침과 함께 너의 가슴을 정확하게 찔렀다. "
            "너는 '오늘은 성이 휴일이었는데...' 라고 중얼거리며 눈을 감았다.",
            knowledge_gained="성 안은 함부로 들어가면 위험하다"
        )

    if st.button("🪨 땅을 파본다"):
        die(
            "열심히 땅을 파고 있었는데, 갑자기 땅속에서 해골이 튀어나왔다. "
            "'내가 묻어둔 보물을 건드리지 마!'라고 외치며 해골이 너의 머리를 주먹으로 세게 내려쳤다. "
            "해골의 펀치는 생각보다 강력했다.",
            knowledge_gained="땅속에는 화난 해골이 살고 있다"
        )

    if st.button("☀️ 하늘을 향해 점프한다"):
        die(
            "기사가 용감하게 하늘을 향해 점프했다. "
            "공중에 잠시 떠 있던 너는 문득 깨달았다. "
            "'아... 나는 날 수 없구나.' "
            "그리고 중력은 냉정하게 너를 바닥으로 끌어당겼다.",
            knowledge_gained="인간은 날 수 없다"
        )

    if st.button("🗡️ 지나가는 상인에게 말을 건다"):
        die(
            "상인에게 다가가 '야, 너 돈 많아 보이는데'라고 인사했다. "
            "상인이 천천히 고개를 들더니, 조용히 칼을 뽑았다. "
            "'오늘 운이 좋구나, 기사여.' "
            "너는 상인의 칼솜씨가 생각보다 훨씬 좋다는 사실을 알게 되었다.",
            knowledge_gained="상인들은 생각보다 싸움을 잘한다"
        )

    if st.button("🧱 성벽을 기어오른다"):
        die(
            "성벽을 열심히 기어오르던 중, 위에서 병사가 고개를 내밀었다. "
            "'아래에 뭐가 있나?' 하며 돌을 하나 떨어뜨렸다. "
            "돌은 정확히 너의 정수리를 맞췄다. "
            "병사는 '아...' 하며 당황한 표정을 지었다.",
            knowledge_gained="성벽 위의 병사는 돌을 잘 던진다"
        )

    if st.button("🕊️ 비둘기에게 식빵을 던져본다"):
        die(
            "광장에 있는 비둘기에게 식빵을 하나 던져주었다. "
            "비둘기가 식빵을 받아먹는 대신, 정확하게 너의 이마를 향해 식빵을 뱉었다. "
            "너는 '비둘기가 왜...' 라고 생각하며 쓰러졌다. "
            "비둘기의 반격은 예상을 훨씬 초월했다.",
            knowledge_gained="비둘기는 식빵을 뱉을 줄 안다"
        )

# ==================== 숲 입구 ====================
elif st.session_state.location == "숲 입구":
    st.write("울창한 숲의 입구다. 나뭇잎 사이로 희미한 새소리와 함께 알 수 없는 기척이 느껴진다.")

    if st.button("🔙 성 앞 광장으로 돌아간다"):
        st.session_state.location = "성 앞 광장"
        st.rerun()

    if st.button("🌳 나무를 흔들어본다"):
        die(
            "나무를 세게 흔들었더니 위에 있던 벌집이 떨어졌다. "
            "수천 마리의 벌이 동시에 너를 발견하고 '오늘은 꿀 대신 기사 피를 마시자!'라고 외쳤다. "
            "벌들의 단결력은 생각보다 강력했다.",
            knowledge_gained="나무를 함부로 흔들면 안 된다"
        )

    if st.button("🦊 이상한 소리가 나는 쪽으로 간다"):
        die(
            "소리가 나는 쪽으로 가보니, 여우 한 마리가 피아노를 치고 있었다. "
            "여우가 너를 보더니 '듣기 싫으면 죽어'라고 말했다. "
            "그리고 피아노 의자를 너에게 정확하게 던졌다. "
            "여우는 생각보다 폭력적이었다.",
            knowledge_gained="여우는 피아노를 칠 줄 안다"
        )

    if st.button("🍄 예쁜 버섯을 먹어본다"):
        die(
            "예쁜 색깔의 버섯을 하나 집어 먹었다. "
            "잠시 후 너는 자신이 나비라고 확신하게 되었다. "
            "'나는 이제 자유롭게 날 수 있어!'라고 외치며 근처 절벽으로 뛰어내렸다. "
            "버섯의 효과는 생각보다 강력했다.",
            knowledge_gained="예쁜 버섯은 절대 먹으면 안 된다"
        )

    if st.button("🕳️ 구멍 속을 들여다본다"):
        die(
            "검은 구멍 속을 들여다보니, 구멍이 갑자기 '뭐 봐?'라고 말했다. "
            "그리고 구멍이 입을 크게 벌리더니 너를 통째로 삼켰다. "
            "구멍은 생각보다 배가 고팠다.",
            knowledge_gained="구멍은 말할 수 있다"
        )

st.markdown("---")
st.caption("💡 대부분의 선택지가 죽음으로 이어집니다. 죽으면서 지식을 쌓아 새로운 가능성을 열어보세요!")

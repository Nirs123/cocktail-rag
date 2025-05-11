import streamlit as st
from util import get_closest_cocktails
from streamlit_extras.stylable_container import stylable_container
from PIL import Image
import requests

st.set_page_config(
    page_title="Recherche Vectorielle de Cocktails",
    page_icon="🍹",
    layout="wide",
)

st.title('Recherche Vectorielle de Cocktails 🍹')

if 'res_index' not in st.session_state:
    st.session_state.res_index = 0
if 'res' not in st.session_state:
    st.session_state.res = [{'name':""}]

def process_request():
    st.session_state.res_index = 0
    st.session_state.res = get_closest_cocktails(request)

@st.dialog(title=f"A propos du cocktail {st.session_state.res[st.session_state.res_index]['name']}")
def get_cocktails_info():
    st.write("\n ".join(st.session_state.res[st.session_state.res_index]['about'].split("; ")))

INPUT_COL, OUTPUT_COL = st.columns([1, 3], gap='small')

with INPUT_COL:
    request = st.text_area('Veuillez entrer votre requête :')
    process = st.button('Rechercher', on_click=process_request)

with OUTPUT_COL:
    if len(st.session_state.res) > 1:
        res_index = st.session_state.res_index
        res = st.session_state.res

        subheader_text = f"Cocktail n°{res_index+1} : {res[res_index]['name']}"
        annotated_tags = [(tag, "") for tag in res[res_index]['tags'].split(";")]

        html_content = f"""
        <div style="display: flex; align-items: center; padding-bottom: 10px;">
            <div style="font-size: 1.5em; font-weight: bold; margin-right: 10px;">{subheader_text}</div>
            <div>{" ".join([f"<span style='background-color: #e26f6f; padding: 2px 5px; border-radius: 5px;'>{tag}</span>" for tag, _ in annotated_tags])}</div>
        </div>
        """
        st.markdown(html_content, unsafe_allow_html=True)

        img_col, desc_col = st.columns([1,2])

        with img_col:
            st.image(
                Image.open(requests.get("https://cocktailmag.fr"+res[res_index]['img_link'], stream=True).raw),
                width=300
            )
            st.button('En savoir plus sur le cocktail', on_click=get_cocktails_info, type='primary')

        with desc_col:
            st.write(res[res_index]['description'])
            st.write("Ingrédients:\n- " + "\n- ".join(res[res_index]['ingredients'].split("; ")))
            st.write("Recette: \n- " + "\n- ".join(res[res_index]['recipe'].split("; ")))

        col1, col2 = st.columns(2)
        with col1:
            with stylable_container(
                key="Upload_Data",
                css_styles="""
                button{
                    float: right;
                }
                """
            ):
                if st.button('<',disabled=st.session_state.res_index == 0):
                    st.session_state.res_index -= 1
                    st.rerun()
        with col2:
            if st.button('\>', disabled=st.session_state.res_index == len(st.session_state.res) - 1):
                st.session_state.res_index += 1
                st.rerun()

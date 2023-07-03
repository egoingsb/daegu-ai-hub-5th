import gradio as gr

ko2enDict = {"사랑": "love", "사자": "lion", "사과": "apple"}
en2koDict = {"love": "사랑", "lion": "사자", "apple": "사과"}
dict = {"ko2en": ko2enDict, "en2ko": en2koDict}


def trans(type, word):
    return dict[type][word]


app = gr.Interface(
    fn=trans,
    inputs=[
        gr.Radio(choices=["ko2en", "en2ko"]),
        gr.Textbox(value="사랑", info="한국어를 입력하세요"),
    ],
    outputs="text",
)
app.launch(debug=True)

print(trans("ko2en", "사랑"))

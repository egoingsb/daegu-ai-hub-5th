import gradio as gr

ko2enDict = {"사랑": "love", "사자": "lion", "사과": "apple"}


def trans(word):
    return ko2enDict[word]


app = gr.Interface(fn=trans, inputs="text", outputs="text")
app.launch(debug=True)

print(trans("사랑"))

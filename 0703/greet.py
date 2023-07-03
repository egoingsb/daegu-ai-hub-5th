import gradio as gr


def greet(name):
    print(name)
    return "hi, " + name


app = gr.Interface(fn=greet, inputs="text", outputs="text")

app.launch(share=True)


# 이름 = input("이름:")
# print(greet(이름))

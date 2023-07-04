import gradio as gr


def add(left, right):
    return int(left) + int(right)


app = gr.Interface(fn=add, inputs=["text", "text"], outputs="text")
app.launch(debug=True)
# input1 = int(input("값1 :"))
# input2 = int(input("값2 :"))
# print(add(input1, input2))

from openai import OpenAI
import base64
from PIL import Image
from io import BytesIO

# LLM Key:
YI_KEY = "78165fbbee234467bd903785f650caf4"


# Chat Online:
def LLM(
        Tips='图片中有一个计算式，请计算一下结果并输出，例如：图中内容为1+1=，你输出为2。图中的内容为2+2=，你输出4。注意，你只输出结果，比如数字2,即最后的输出一定是一个数字，除了数字一定不要展示其他内容,我只要输出的数字格式为单个字符 例如X=8，在终端输出的格式为“结果：最终的数字”',
        img_path='./img_dir/Plus.png'):
    # Ask for Survice Server:
    client = OpenAI(
        api_key=YI_KEY,
        base_url="https://api.lingyiwanwu.com/v1"
    )

    # Encode to be Base64:
    with open(img_path, 'rb') as image_file:
        image = 'data:image/jpeg;base64,' + base64.b64encode(image_file.read()).decode('utf-8')

    # Split String with ',':
    head, context = image.split(",")

    # Tip1:
    PROMPT1 = '请你帮我求解这道数学题，给出分析的过程与最终结果，不要使用LaTeX语言。结果应该是正整数，如1、2、3等大于零的整数。否则说明你错了。'

    # Ask For Service Server:
    completion = client.chat.completions.create(
        model="yi-vision",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": PROMPT1
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image
                        }
                    }
                ]
            },
        ]
    )

    # Get Result1:
    result_str = completion.choices[0].message.content.strip()
    result = str(result_str)

    # Echo result1:
    print('retult1: ', result)

    # Tip2:
    PROMPT2 = '请你帮我看看下边这段话，这是对某个数学题的求解过程，请你告诉我数学题的最终结果。注意，除了数字一定不要展示其他内容,我只要输出的格式为单个或多个字符！此外，最终结果不要是LaTeX语言格式！'

    # Ask For Service Server:
    completion = client.chat.completions.create(
        model="yi-vision",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": PROMPT2
                    },
                    {
                        "type": "text",
                        "text": result
                    }
                ]
            },
        ]
    )

    # Get Consequent result:
    result_str = completion.choices[0].message.content.strip()
    result = str(result_str)

    # Decode img_Base64 to Image:
    img_data = base64.b64decode(context)
    image_toshow = Image.open(BytesIO(img_data))

    # show:
    image_toshow.show()

    return result


# Mainwork:
if __name__ == '__main__':
    try:
        # Chat TO the LLM Online:
        result = LLM()

        # Echo:
        print('大模型调用成功！')
        print('最终结果:', result)
    except Exception as e:
        print(e)

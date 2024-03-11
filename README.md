import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="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",
)
message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0,
    system="you a great ai helper",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "hi"
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": "hello"
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "hi，what about love"
                }
            ]
        }
    ]
)
print(message.content)

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

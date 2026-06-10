from src.agent.assistant import Assistant

def main():
    client = Assistant()

    print(client.ask(input()))


if __name__ == "__main__":
    main()

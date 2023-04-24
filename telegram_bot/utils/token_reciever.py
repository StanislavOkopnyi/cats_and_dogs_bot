def main():
    TOKEN = input("Enter the bot token: ")
    with open("token.conf", "w") as f:
        f.write(TOKEN)


if __name__ == "__main__":
    main()

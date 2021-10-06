import torch


def main():
    print("hello")

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(device)


if __name__ == "__main__":
    main()
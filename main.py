from game_engine import GameEngine

def main():
    print("=" * 50)
    print("🏰AGE OF TERMINAL🫅")
    print("=" * 50)
    print()
    input("Press Enter to start YOUR kingdown age")

    game = GameEngine()
    game.run()

    print("\nUntil tomorrow commander!")

if __name__ == "__main__": #Boa prática. Evita que outra instância execute, caso importe algo desse arquivo. Apesar do arquivo não ter nada útil além do próprio trigger do jogo.
    main()
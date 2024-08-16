# Simulação de Back End
class Backend:
    def __init__(self):
        self.users = []

    def add_user(self, name, age):
        if self._validate_user(name, age):
            user = {"name": name, "idade": age}
            self.users.append(user)
            return "User adicionado com sucesso!"
        else:
            return "Dado inválido."

    def _validate_user(self, name, age):
        return isinstance(name, str) and isinstance(age, int) and age > 0

    def get_users(self):
        return self.users

# Simulação de Front End
class Frontend:
    def __init__(self, backend):
        self.backend = backend

    def display_menu(self):
        while True:
            print("\n1. Adicionar Usuário")
            print("2. Exibir Usuários")
            print("3. Sair")
            choice = input("Escolha uma opção: ")

            if choice == '1':
                self.add_user()
            elif choice == '2':
                self.show_users()
            elif choice == '3':
                print("Saindo...")
                break
            else:
                print("Opção inválida! Tente novamente.")

    def add_user(self):
        name = input("Digite o nome do usuário: ")
        age = int(input("Digite a idade do usuário: "))
        result = self.backend.add_user(name, age)
        print(result)

    def show_users(self):
        users = self.backend.get_users()
        if users:
            print("\nLista de Usuários:")
            for user in users:
                print(f"Nome: {user['name']}, Idade: {user['age']}")
        else:
            print("Nenhum usuário cadastrado.")

# Inicialização do sistema
if __name__ == "__main__":
    backend = Backend()
    frontend = Frontend(backend)
    frontend.display_menu()

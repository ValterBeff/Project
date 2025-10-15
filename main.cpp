#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <conio.h> // Para getch() no Windows

#define MAX_SENHA 20  // Tamanho máximo permitido para a senha

int main() {
    FILE *arquivo;
    char senhaCorreta[MAX_SENHA + 1];
    char senhaDigitada[MAX_SENHA + 1];
    int i = 0;
    char c;

    // === 1. LEITURA DA SENHA CORRETA DO ARQUIVO ===
    arquivo = fopen("senha.txt", "r");
    if (arquivo == NULL) {
        printf("Erro: arquivo 'senha.txt' não encontrado!\n");
        return 1; // Encerra o programa
    }

    // Lê a senha armazenada (apenas a primeira linha)
    if (fgets(senhaCorreta, sizeof(senhaCorreta), arquivo) == NULL) {
        printf("Erro ao ler o arquivo 'senha.txt'.\n");
        fclose(arquivo);
        return 1;
    }
    fclose(arquivo);

    // Remove o '\n' do final da senha lida, caso exista
    senhaCorreta[strcspn(senhaCorreta, "\n")] = '\0';

    // === 2. ENTRADA DA SENHA DO USUÁRIO ===
    printf("Digite a senha: ");

    i = 0;
    while (1) {
        c = getch(); // Captura um caractere sem exibir

        // Quando o usuário pressionar ENTER (13 no Windows)
        if (c == 13) {
            senhaDigitada[i] = '\0'; // Finaliza a string
            break;
        }

        // Permitir uso do Backspace
        else if (c == 8) { // Código ASCII do Backspace
            if (i > 0) {
                i--;
                printf("\b \b"); // Apaga o último asterisco
            }
        }

        // Adicionar caractere à senha (com limite)
        else if (i < MAX_SENHA) {
            senhaDigitada[i++] = c;
            printf("*"); // Exibe máscara
        }
    }

    printf("\n");

    // === 3. COMPARAÇÃO DAS SENHAS ===
    if (strcmp(senhaDigitada, senhaCorreta) == 0) {
        printf("Senha correta! Acesso permitido.\n");
    } else {
        printf("Senha incorreta! Acesso negado.\n");
    }

    return 0;
}


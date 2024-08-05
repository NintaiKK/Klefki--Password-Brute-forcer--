import itertools
import string
import time

def brute_force(target_password, max_attempts=10000000, pause_duration=0):
    chars =string.ascii_lowercase
    attempts = 0
    total_attempts = 0
    found_password = None
    start_time = time.time()

    # Loop sobre comprimentos de senha de 1 a 8 caracteres
    for length in range(8,9):  # Ajuste o comprimento máximo conforme necessário
        # Gerar combinações de caracteres
        for guess in itertools.product(chars, repeat=length):
            guess_password = ''.join(guess)
            attempts += 1
            total_attempts += 1

            if guess_password == target_password:
                found_password = guess_password
                break
            
            # Verifica se atingiu o limite de tentativas
            if attempts >= max_attempts:
                print(f'Total de tentativas {total_attempts}')
                print(f'Última tentativa {guess_password}')
                time.sleep(pause_duration)
                attempts = 0  # Resetar o contador de tentativas

        if found_password:
            break

    end_time = time.time()  # Mover o temporizador para cá
    duracao = end_time - start_time  # Calcular a duração
    print(f'senha: {found_password}, total de tentativas: {total_attempts}, duração do processo: {duracao}')
    return

# Exemplo de uso
target_password = "aprocont"  # Substitua pela senha que deseja encontrar
found_password = brute_force(target_password)

#!/usr/bin/env python3
"""
Script de teste para demonstrar o uso da API Pac Lead
Execute este script com a API rodando em http://localhost:8000
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_api():
    print("🚀 Testando API Pac Lead\n")
    
    # 1. Registrar usuário
    print("1. Registrando usuário...")
    user_data = {
        "email": "teste@exemplo.com",
        "password": "senha123",
        "full_name": "João Silva",
        "company_name": "Empresa Teste",
        "ai_tone": "Seja amigável e entusiasmado ao falar sobre nossos produtos!"
    }
    
    response = requests.post(f"{BASE_URL}/auth/register", json=user_data)
    if response.status_code == 201:
        print("✅ Usuário registrado com sucesso!")
        user_id = response.json()["id"]
    else:
        print(f"❌ Erro ao registrar: {response.text}")
        return
    
    # 2. Fazer login
    print("\n2. Fazendo login...")
    login_data = {
        "email": "teste@exemplo.com",
        "password": "senha123"
    }
    
    response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
    if response.status_code == 200:
        token = response.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}
        print("✅ Login realizado com sucesso!")
    else:
        print(f"❌ Erro no login: {response.text}")
        return
    
    # 3. Criar produto
    print("\n3. Criando produto...")
    product_data = {
        "name": "Smartphone XYZ",
        "description": "Smartphone top de linha com câmera de 108MP",
        "price": 1299.99,
        "category": "Eletrônicos",
        "features": "Tela AMOLED 6.7', 256GB, 12GB RAM, Câmera 108MP",
        "benefits": "Fotos profissionais, performance excepcional, bateria que dura o dia todo",
        "target_audience": "Jovens e profissionais que valorizam tecnologia"
    }
    
    response = requests.post(f"{BASE_URL}/products/", json=product_data, headers=headers)
    if response.status_code == 201:
        print("✅ Produto criado com sucesso!")
    else:
        print(f"❌ Erro ao criar produto: {response.text}")
        return
    
    # 4. Listar produtos
    print("\n4. Listando produtos...")
    response = requests.get(f"{BASE_URL}/products/", headers=headers)
    if response.status_code == 200:
        products = response.json()
        print(f"✅ {len(products)} produto(s) encontrado(s)")
    else:
        print(f"❌ Erro ao listar produtos: {response.text}")
        return
    
    # 5. Testar webhook
    print("\n5. Testando webhook...")
    webhook_data = {
        "mensagem": "Quais smartphones vocês têm disponíveis?",
        "user_id": user_id
    }
    
    response = requests.post(f"{BASE_URL}/webhook/", json=webhook_data)
    if response.status_code == 200:
        ai_response = response.json()["resposta"]
        print("✅ Webhook funcionando!")
        print(f"🤖 Resposta da IA: {ai_response}")
    else:
        print(f"❌ Erro no webhook: {response.text}")
    
    print("\n🎉 Todos os testes concluídos!")

if __name__ == "__main__":
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("❌ Erro: Não foi possível conectar à API.")
        print("Certifique-se de que a API está rodando em http://localhost:8000")
        print("Execute: python run.py")


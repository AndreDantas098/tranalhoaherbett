print("voce não tem connta. preencha as seguintes ablyue")
nome = (input ("Nome: "))
email = (input ("Email: "))
senha = (input ("Senha: "))
print("Para acessar o site, faca o LOGIN")
emailatual = (input("digite seu email: "))
while emailatual != email:
    print("corno")
    emailatual = (input("digite seu email: "))

senhaatual = (input("digite sua senha: "))
while senhaatual != senha:
    print("cornosenha")
    senhaatual = (input("digite sua senha: "))
print("ola, %s"%nome,"bem vindo ao nosso site, que serviço gostaria de usufruir?")
import csv
import os

# 1. A CLASSE DEVE VIR PRIMEIRO
class OrcamentoImobiliaria:
    def __init__(self):
        self.valor_base = 0
        self.valor_total_aluguel = 0
        self.valor_contrato = 2000.00
        self.parcelas_escolhidas = 1
        self.tipo_imovel = ""
        self.detalhes_custos = []

    def definir_valor_base(self, tipo):
        self.tipo_imovel = tipo.lower()
        if self.tipo_imovel == "apartamento":
            self.valor_base = 700.00
        elif self.tipo_imovel == "casa":
            self.valor_base = 900.00
        elif self.tipo_imovel == "estudio":
            self.valor_base = 1200.00
        
        self.valor_total_aluguel = self.valor_base
        self.detalhes_custos.append(f"Valor Base ({tipo.capitalize()}): R$ {self.valor_base:.2f}")

    def calcular_adicional_quartos(self, qtd_quartos):
        if self.tipo_imovel != "estudio" and qtd_quartos == 2:
            valor_extra = 200.00 if self.tipo_imovel == "apartamento" else 250.00
            self.valor_total_aluguel += valor_extra
            self.detalhes_custos.append(f"Adicional 2 Quartos: R$ {valor_extra:.2f}")

    def calcular_adicional_vagas(self, qtd_vagas):
        if qtd_vagas > 0:
            if self.tipo_imovel in ["apartamento", "casa"]:
                self.valor_total_aluguel += 300.00
                self.detalhes_custos.append("Adicional Garagem (Casa/Apto): R$ 300.00")
            elif self.tipo_imovel == "estudio":
                custo_garagem = 250.00
                if qtd_vagas > 2:
                    custo_garagem += (qtd_vagas - 2) * 60.00
                self.valor_total_aluguel += custo_garagem
                self.detalhes_custos.append(f"Garagem Estúdio ({qtd_vagas} vagas): R$ {custo_garagem:.2f}")

    def aplicar_desconto_crianca(self, tem_crianca):
        if self.tipo_imovel == "apartamento" and tem_crianca.lower() == "não":
            desconto = self.valor_total_aluguel * 0.05
            self.valor_total_aluguel -= desconto
            self.detalhes_custos.append(f"Desconto (Sem crianças): - R$ {desconto:.2f}")

    def gerar_csv(self, nome_arquivo="orcamento_aluguel.csv"):
        valor_parcela = self.valor_contrato / self.parcelas_escolhidas
        # O modo 'w' garante que o arquivo antigo seja apagado (limpo)
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Mes', 'Valor Aluguel', 'Parcela Contrato', 'Total Mensal'])
            for mes in range(1, 13):
                p_contrato = valor_parcela if mes <= self.parcelas_escolhidas else 0.0
                total_mes = self.valor_total_aluguel + p_contrato
                writer.writerow([mes, f"{self.valor_total_aluguel:.2f}", f"{p_contrato:.2f}", f"{total_mes:.2f}"])
        print(f"\n✅ Planilha '{nome_arquivo}' gerada com sucesso.")

# 2. FUNÇÕES DE SUPORTE
def obter_entrada_valida(msg, opcoes):
    while True:
        res = input(msg).strip().lower()
        if res in [o.lower() for o in opcoes]: return res
        print(f"❌ Opção inválida! Escolha: {', '.join(opcoes)}")

def obter_num_valido(msg, mini, maxi):
    while True:
        try:
            n = int(input(msg))
            if mini <= n <= maxi: return n
            print(f"❌ Digite entre {mini} e {maxi}.")
        except: print("❌ Digite um número.")

# 3. FUNÇÃO PRINCIPAL
def main():
    sistema = OrcamentoImobiliaria()
    print("\n" + "="*50 + "\n      SISTEMA DE ORÇAMENTO - IMOBILIÁRIA R.M\n" + "="*50)
    
    tipo = obter_entrada_valida("Tipo de imóvel (Apartamento, Casa, Estudio): ", ["Apartamento", "Casa", "Estudio"])
    sistema.definir_valor_base(tipo)
    
    if tipo != "estudio":
        quartos = obter_num_valido("Quantidade de quartos (1 ou 2): ", 1, 2)
        sistema.calcular_adicional_quartos(quartos)
    
    vagas = obter_num_valido("Quantidade de vagas de garagem? ", 0, 10)
    sistema.calcular_adicional_vagas(vagas)
    
    if tipo == "apartamento":
        crianca = obter_entrada_valida("Possui crianças? (Sim/Não): ", ["Sim", "Não"])
        sistema.aplicar_desconto_crianca(crianca)

    print(f"\nValor do Contrato: R$ {sistema.valor_contrato:.2f}")
    if obter_entrada_valida("Deseja parcelar o contrato? (Sim/Não): ", ["Sim", "Não"]) == "sim":
        sistema.parcelas_escolhidas = obter_num_valido("Em quantas parcelas? (Em até 5x): ", 2, 5)

    print("\n📋 DESCRIÇÃO DO ORÇAMENTO:")
    for item in sistema.detalhes_custos: print(f"  > {item}")
    print(f"\n💰 VALOR MENSAL: R$ {sistema.valor_total_aluguel:.2f}")
    
    sistema.gerar_csv()
    
    # ABRE O EXCEL AUTOMATICAMENTE
    os.startfile("orcamento_aluguel.csv")

# 4. EXECUÇÃO
if __name__ == "__main__":
    main()
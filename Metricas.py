def calcular_metrica(vp, vn, fp, fn):
    # Cálculo das métricas
    acuracia = (vp + vn) / (vp + vn + fp + fn)
    precisao = vp / (vp + fp)
    sensibilidade = vp / (vp + fn)
    especificidade = vn / (vn + fp)
    f_score = 2 * (precisao * sensibilidade) / (precisao + sensibilidade)

    return {
        "Acurácia": acuracia,
        "Precisão": precisao,
        "Sensibilidade (Recall)": sensibilidade,
        "Especificidade": especificidade,
        "F-score": f_score
    }

# Valores da matriz de confusão
vp = 217
vn = 827
fp = 93
fn = 259

metricas = calcular_metrica(vp, vn, fp, fn)
for metrica, valor in metricas.items():
    print(f"{metrica}: {valor}")

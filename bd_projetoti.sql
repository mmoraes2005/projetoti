create database bd_projetoti;
use bd_projetoti;

CREATE TABLE sustentabilidade (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE,
    consumo_agua VARCHAR(30),
    consumo_energia VARCHAR(30),
    geracao_residuos VARCHAR(30),
    residuos_reciclaveis VARCHAR(30),
    uso_transporte VARCHAR(30)
);

INSERT INTO sustentabilidade (data, consumo_agua, consumo_energia, geracao_residuos, residuos_reciclaveis, uso_transporte) VALUES ('2025-03-24','Moderada Sustentabilidade','Alta Sustentabilidade','Alta Sustentabilidade','Baixa Sustentabilidade','Baixa Sustentabilidade');

drop table sustentabilidade;

SELECT * FROM sustentabilidade;

SELECT
    -- Consumo de água
    CASE 
        WHEN COUNT(DISTINCT consumo_agua) = 1 AND MAX(consumo_agua) = 'Alta Sustentabilidade' THEN 'Alta Sustentabilidade'
        WHEN COUNT(DISTINCT consumo_agua) = 1 AND MAX(consumo_agua) = 'Baixa Sustentabilidade' THEN 'Baixa Sustentabilidade'
        ELSE 'Moderada Sustentabilidade'
    END AS media_consumo_agua,

    -- Consumo de energia
    CASE 
        WHEN COUNT(DISTINCT consumo_energia) = 1 AND MAX(consumo_energia) = 'Alta Sustentabilidade' THEN 'Alta Sustentabilidade'
        WHEN COUNT(DISTINCT consumo_energia) = 1 AND MAX(consumo_energia) = 'Baixa Sustentabilidade' THEN 'Baixa Sustentabilidade'
        ELSE 'Moderada Sustentabilidade'
    END AS media_consumo_energia,

    -- Geração de resíduos
    CASE 
        WHEN COUNT(DISTINCT geracao_residuos) = 1 AND MAX(geracao_residuos) = 'Alta Sustentabilidade' THEN 'Alta Sustentabilidade'
        WHEN COUNT(DISTINCT geracao_residuos) = 1 AND MAX(geracao_residuos) = 'Baixa Sustentabilidade' THEN 'Baixa Sustentabilidade'
        ELSE 'Moderada Sustentabilidade'
    END AS media_geracao_residuos,

    -- Uso de transporte
    CASE 
        WHEN COUNT(DISTINCT uso_transporte) = 1 AND MAX(uso_transporte) = 'Alta Sustentabilidade' THEN 'Alta Sustentabilidade'
        WHEN COUNT(DISTINCT uso_transporte) = 1 AND MAX(uso_transporte) = 'Baixa Sustentabilidade' THEN 'Baixa Sustentabilidade'
        ELSE 'Moderada Sustentabilidade'
    END AS media_uso_transporte

FROM sustentabilidade;

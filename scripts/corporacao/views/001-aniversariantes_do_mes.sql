CREATE OR REPLACE VIEW aniversariantes_do_mes as SELECT
	f.codigo,
	f.nome,
    f.nascimento
FROM
	funcionario f
where
	month(f.nascimento) = month(now());
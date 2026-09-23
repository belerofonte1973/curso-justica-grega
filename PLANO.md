# Curso: Justiça e seus Cognatos na Literatura Grega

## Visão Geral

Curso enciclopédico sobre o conceito de justiça (δίκη, θέμις, αἰδώς, νόμος, δικαιοσύνη) na literatura grega, abrangendo poesia arcaica, tragédia, história, filosofia e retórica.

**Formato:** Website acadêmico interativo (Astro + Starlight)
**Idioma:** PT-BR
**Conteúdo:** ~12 módulos, ~50 páginas de conteúdo

---

## Módulos do Curso

### Módulo 1 — Fundamentos Conceituais
1.1. Δίκη (Díkai): justiça, ordem, costume, julgamento
1.2. Θέμις (Themis): lei divina, ordem cósmica, tradição sagrada
1.3. Αἰδώς (Aidôs): vergonha, respeito, honra
1.4. Νόμος (Nomos): lei, costume, convenção
1.5. Δικαιοσύνη (Dikaiosýne): justiça como virtude

### Módulo 2 — A Poesia Arcaica: Homero
2.1. A *Ilíadi* e a ira de Aquiles: justiça e honra
2.2. A *Odisseia* e o retorno: justiça e vingança
2.3. O julgamento de Páris: justiça divina
2.4. Aquiles e Príamo: piedade e justiça

### Módulo 3 — A Poesia Arcaica: Hesíodo
3.1. *Os Trabalhos e os Dias*: justiça e trabalho
3.2. *Teogonia*: Dike como filha de Zeus e Têmis
3.3. O mito das cinco raças: justiça e decadência
3.4. O canto do falcão e do rouxinol: injustiça e poder

### Módulo 4 — A Poesia Lírica e o Iambo
4.1. Sólon: eunomia e justiça cívica
4.2. Teognis: justiça e desigualdade
4.3. Píndaro: justiça e vitória
4.4. Arquiloco: justiça e vingança pessoal

### Módulo 5 — A Tragédia: Ésquilo
5.1. *Oresteia*: vingança, justiça e o nascimento do tribunal
5.2. *Prometeu Acorrentado*: justiça divina e tirania
5.3. *Os Persas*: justiça e hybris imperial
5.4. O Areópago: da vingança à lei

### Módulo 6 — A Tragédia: Sófocles
6.1. *Édipo Rei*: justiça, culpa e destino
6.2. *Antígona*: lei divina vs. lei humana
6.3. *Ajax*: justiça e loucura
6.4. *Filoctetes*: justiça e traição

### Módulo 7 — A Tragédia: Eurípides
7.1. *Medeia*: justiça e vingança feminina
7.2. *Hécuba*: justiça e desumanização
7.3. *As Troianas*: guerra e injustiça
7.4. *Orestes*: justiça e instabilidade política

### Módulo 8 — A História
8.1. Heródoto: justiça e liberdade (Histórias, Livros I-V)
8.2. Tucídides: justiça e poder (Melos, Expedição à Sicília)
8.3. Xenofonte: justiça e liderança (Ciro, Agesilau)
8.4. Políbio: justiça e constituição mista

### Módulo 9 — A Filosofia: Platão
9.1. *República*: justiça como harmonia da alma e da cidade
9.2. *Górgias*: justiça e retórica
9.3. *Leis*: justiça e legislação
9.4. *Apologia*: justiça e dever cívico

### Módulo 10 — A Filosofia: Aristóteles
10.1. *Ética a Nicômaco*: justiça como virtude
10.2. *Política*: justiça e constituição
10.3. *Retórica*: justiça e persuasão
10.4. Justiça distributiva e corretiva

### Módulo 11 — A Retórica e o Direito
11.1. Antifonte: justiça e discurso
11.2. Demóstenes: justiça e democracia
11.3. Isócrates: justiça e pan-helenismo
11.4. Lísias: justiça e vida cotidiana

### Módulo 12 — Síntese e Recepção
12.1. A evolução do conceito: de Homero a Aristóteles
12.2. Justiça e cristianismo: de Paulo a Agostinho
12.3. Justiça na modernidade: de Hobbes a Rawls
12.4. Justiça e gênero: leituras contemporâneas

---

## Estrutura Técnica

```
curso-justica-grega/
├── astro.config.mjs
├── package.json
├── src/
│   ├── content.config.ts
│   ├── content/docs/
│   │   ├── index.mdx
│   │   ├── modulo-1/ ... modulo-12/
│   │   ├── recursos/
│   │   └── sobre.mdx
│   └── styles/
├── scripts/verificar-site.py
├── netlify.toml
└── README.md
```

## Calibração

- Modelo principal: longcat-2.0:free (1M ctx)
- Subagentes: deepseek-v4-flash (reasoning high)
- Profundidade: aprovado (triangulação de fontes)
- Idioma: PT-BR
- Citação: autor, ano, p.X — sempre que possível

---

**Data de criação:** 22/09/2026
**Versão:** 1.0

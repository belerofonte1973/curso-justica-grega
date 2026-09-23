import os
import re
import sys
from pathlib import Path

# Configuração
DOCS_DIR = Path("src/content/docs")
REQUIRED_FILES = ["index.mdx", "sobre.mdx", "recursos/index.mdx"]
REQUIRED_MODULES = [f"modulo-{i}/index.mdx" for i in range(1, 13)]
GREEK_TERMS = ["Δίκη", "δίκη", "θέμις", "Θέμις", "αἰδώς", "νόμος", "δικαιοσύνη", "díkē", "têmis", "aidôs", "nómos", "dikaiosýne"]
PORTUGUESE_MARKERS = ["você", "não", "mais", "também", "entre", "sobre", "após", "através"]
SPANISH_MARKERS = [" el ", " los ", " las ", " del ", " es ", " son ", " pero ", " porque "]

def check_file_structure():
    """Verifica se a estrutura de arquivos está completa."""
    print("=" * 60)
    print("VERIFICAÇÃO DE INTEGRIDADE DO SITE")
    print("=" * 60)
    
    missing = []
    
    for f in REQUIRED_FILES + REQUIRED_MODULES:
        path = DOCS_DIR / f
        if not path.exists():
            missing.append(f)
    
    if missing:
        print(f"\n❌ ARQUIVOS FALTANDO ({len(missing)}):")
        for f in missing:
            print(f"   - {f}")
        return False
    
    print(f"\n✓ Todos os {len(REQUIRED_FILES) + len(REQUIRED_MODULES)} arquivos principais encontrados.")
    return True

def check_greek_terms():
    """Verifica se os termos gregos estão presentes."""
    print("\n—" * 30)
    print("VERIFICAÇÃO DE TERMOS GREGOS")
    print("—" * 30)
    
    all_files = list(DOCS_DIR.rglob("*.mdx"))
    terms_found = []
    
    for f in all_files:
        content = f.read_text(encoding="utf-8")
        for term in GREEK_TERMS:
            if term in content:
                terms_found.append(term)
    
    if terms_found:
        unique = sorted(set(terms_found))
        print(f"✓ Termos gregos encontrados: {', '.join(unique)}")
        return True
    else:
        print("⚠ Nenhum termo grego encontrado. Isso pode indicar problemas.")
        return False

def check_portuguese():
    """Verifica marcadores de português e detecta espanhol."""
    print("\n—" * 30)
    print("VERIFICAÇÃO DE IDIOMA (PT-BR)")
    print("—" * 30)
    
    all_files = list(DOCS_DIR.rglob("*.mdx"))
    pt_score = 0
    es_score = 0
    
    for f in all_files[:20]:  # Amostragem
        content = f.read_text(encoding="utf-8")
        for m in PORTUGUESE_MARKERS:
            pt_score += content.lower().count(m)
        for m in SPANISH_MARKERS:
            es_score += content.lower().count(m)
    
    print(f" Marcadores PT-BR encontrados: {pt_score}")
    print(f" Marcadores de espanhol: {es_score}")
    
    if pt_score > es_score:
        print("✓ Idioma principal: Português brasileiro")
        return True
    else:
        print("⚠ Possível conteúdo em espanhol detectado!")
        return False

def check_citations():
    """Verifica se há citações acadêmicas (inline ou bibliográficas)."""
    print("\n" + "—" * 30)
    print("VERIFICAÇÃO DE CITAÇÕES ACADÊMICAS")
    print("—" * 30)
    
    # Citações inline: (Autor, Ano) ou (Autor & Autor, Ano)
    inline_pattern = re.compile(r'\([A-Z][a-z]+(?:\s+(?:&\s+)?[A-Z][a-z]+)*,?\s+\d{4}')
    # Citações bibliográficas: Autor, Ano
    bib_pattern = re.compile(r'[A-Z][a-z]+,?\s+\d{4}')
    
    files_with_citations = 0
    total_citations = 0
    
    for f in DOCS_DIR.rglob("*.mdx"):
        content = f.read_text(encoding="utf-8")
        inline_matches = inline_pattern.findall(content)
        bib_matches = bib_pattern.findall(content)
        total = len(inline_matches) + len(bib_matches)
        if total > 0:
            files_with_citations += 1
            total_citations += total
    
    print(f" Arquivos com citações: {files_with_citations}")
    print(f" Total de citações (inline + bibliográficas): {total_citations}")
    
    if total_citations > 0:
        print("✓ Citações acadêmicas encontradas")
        return True
    else:
        print("⚠ Nenhuma citação acadêmica encontrada!")
        return False

def main():
    """Executa todas as verificações."""
    results = []
    results.append(("Estrutura de arquivos", check_file_structure()))
    results.append(("Termos gregos", check_greek_terms()))
    results.append(("Idioma português", check_portuguese()))
    results.append(("Citações acadêmicas", check_citations()))
    
    print("\n" + "=" * 60)
    print("RESULTADO FINAL")
    print("=" * 60)
    
    passed = sum(1 for _, r in results if r)
    total = len(results)
    
    for name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"  {status} {name}")
    
    print(f"\n {passed}/{total} verificações passaram")
    
    if passed == total:
        print("\n🎉 TUDO CERTO! O site está pronto.")
        return 0
    else:
        print(f"\n⚠ {total - passed} verificação(ões) falharam. Corrija antes de publicar.")
        return 1

if __name__ == "__main__":
    sys.exit(main())

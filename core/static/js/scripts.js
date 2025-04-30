/**
 * StudyCode - Scripts principais
 * Funcionalidades JavaScript para aprimorar a experiência do usuário
 */

// Função executada quando o DOM estiver carregado
document.addEventListener('DOMContentLoaded', function() {
    // Inicializa os tooltips do Bootstrap
    initTooltips();
    
    // Inicializa o campo de tags
    initTagsInput();
    
    // Adiciona comportamento de auto-expansão para textareas
    initAutoResizeTextareas();
    
    // Inicializa o filtro de pesquisa dinâmico
    initDynamicSearch();
    
    // Inicializa a validação de formulários
    initFormValidation();
    
    // Inicializa o highlight de código nos blocos de código
    highlightCodeBlocks();
    
    // Inicializa o sistema de cópia de código com um clique
    initCodeCopyButtons();
});

/**
 * Inicializa os tooltips do Bootstrap
 */
function initTooltips() {
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));
}

/**
 * Inicializa o comportamento do campo de tags
 */
function initTagsInput() {
    const tagsInput = document.getElementById('tags');
    if (!tagsInput) return;
    
    // Adiciona comportamento para formatar as tags ao digitar
    tagsInput.addEventListener('input', function() {
        // Remove espaços extras e garante que as tags estejam separadas por vírgulas
        let value = this.value.replace(/\s*,\s*/g, ',');
        
        // Atualiza o valor do campo
        this.value = value;
    });
    
    // Formata as tags ao perder o foco
    tagsInput.addEventListener('blur', function() {
        // Remove vírgulas no início e fim
        let value = this.value.replace(/^,|,$/g, '');
        
        // Atualiza o valor do campo
        this.value = value;
    });
}

/**
 * Inicializa o comportamento de auto-expansão para textareas
 */
function initAutoResizeTextareas() {
    const textareas = document.querySelectorAll('textarea');
    
    textareas.forEach(textarea => {
        textarea.addEventListener('input', function() {
            // Reset height to auto to get the right scrollHeight
            this.style.height = 'auto';
            // Set the height to the scrollHeight
            this.style.height = (this.scrollHeight) + 'px';
        });
        
        // Trigger the event on load to adjust initial content
        const event = new Event('input');
        textarea.dispatchEvent(event);
    });
}

/**
 * Inicializa o editor de código com highlight de sintaxe
 */
function initCodeEditor() {
    const codeEditors = document.querySelectorAll('.code-editor');
    
    codeEditors.forEach(editor => {
        // Adiciona comportamentos especiais ao editor de código
        editor.addEventListener('keydown', function(e) {
            // Implementa indentação com Tab
            if (e.key === 'Tab') {
                e.preventDefault();
                
                // Seleciona a posição atual do cursor
                const start = this.selectionStart;
                const end = this.selectionEnd;
                
                // Insere o tab
                this.value = this.value.substring(0, start) + '    ' + this.value.substring(end);
                
                // Move o cursor após o tab
                this.selectionStart = this.selectionEnd = start + 4;
            }
        });
    });
}

/**
 * Adiciona highlight de sintaxe aos blocos de código
 */
function highlightCodeBlocks() {
    const codeBlocks = document.querySelectorAll('.code-block code');
    
    codeBlocks.forEach(block => {
        // Aqui poderíamos integrar uma biblioteca como highlight.js se estivesse disponível
        // Por enquanto, aplicamos uma formatação básica com CSS
        
        // Formata comentários
        block.innerHTML = block.innerHTML
            .replace(/(\/\/.*)/g, '<span class="code-comment">$1</span>')
            .replace(/(\/\*[\s\S]*?\*\/)/g, '<span class="code-comment">$1</span>')
            .replace(/(\#.*)/g, '<span class="code-comment">$1</span>');
            
        // Formata strings
        block.innerHTML = block.innerHTML
            .replace(/(".*?")/g, '<span class="code-string">$1</span>')
            .replace(/('.*?')/g, '<span class="code-string">$1</span>')
            .replace(/(`.*?`)/g, '<span class="code-string">$1</span>');
            
        // Formata palavras-chave (exemplo básico)
        const keywords = ['def', 'class', 'function', 'if', 'else', 'for', 'while', 'return', 'import', 'from', 'var', 'let', 'const'];
        keywords.forEach(keyword => {
            const regex = new RegExp(`\\b(${keyword})\\b`, 'g');
            block.innerHTML = block.innerHTML.replace(regex, '<span class="code-keyword">$1</span>');
        });
    });
}

/**
 * Adiciona botões para copiar o código com um clique
 */
function initCodeCopyButtons() {
    const codeBlocks = document.querySelectorAll('.code-block');
    
    codeBlocks.forEach(block => {
        // Cria o botão de cópia
        const copyButton = document.createElement('button');
        copyButton.className = 'copy-button';
        copyButton.innerHTML = 'Copiar';
        copyButton.setAttribute('title', 'Copiar para a área de transferência');
        
        // Adiciona o botão ao bloco de código
        block.style.position = 'relative';
        block.appendChild(copyButton);
        
        // Adiciona o evento de clique
        copyButton.addEventListener('click', function() {
            // Seleciona o texto do bloco
            const code = block.querySelector('code').innerText;
            
            // Copia o texto para a área de transferência
            navigator.clipboard.writeText(code).then(() => {
                // Feedback visual
                copyButton.innerHTML = 'Copiado!';
                copyButton.classList.add('copied');
                
                // Volta ao estado original após 1.5 segundos
                setTimeout(() => {
                    copyButton.innerHTML = 'Copiar';
                    copyButton.classList.remove('copied');
                }, 1500);
            });
        });
    });
}

/**
 * Inicializa o filtro de pesquisa dinâmico
 */
function initDynamicSearch() {
    const searchForm = document.querySelector('form[action*="pesquisa"]');
    const searchInput = document.querySelector('input[name="q"]');
    
    if (searchForm && searchInput) {
        // Adiciona um pequeno delay para não sobrecarregar com muitas requisições
        let searchTimeout;
        
        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            
            // Aguarda 300ms após o usuário parar de digitar
            searchTimeout = setTimeout(() => {
                // Aqui poderíamos implementar uma pesquisa em AJAX
                // Para uma implementação completa, isso seria feito no backend
                // Esta é uma simulação simplificada para o frontend
                
                // Na implementação real, isso enviaria uma requisição AJAX
                // e atualizaria os resultados dinamicamente
                
                // Para esta demonstração, apenas destacamos termos pesquisados
                highlightSearchTerms(this.value);
            }, 300);
        });
    }
}

/**
 * Destaca os termos pesquisados nos resultados
 */
function highlightSearchTerms(searchTerm) {
    if (!searchTerm) return;
    
    const resultItems = document.querySelectorAll('#resultados-lista .list-group-item');
    
    resultItems.forEach(item => {
        // Busca pelo termo nos títulos e descrições
        const titulo = item.querySelector('.item-titulo');
        const descricao = item.querySelector('p');
        
        if (titulo && descricao) {
            // Esta é uma implementação simplificada - apenas visual
            // Numa implementação real, isso seria feito no servidor
            
            // Verifica se o termo está no título ou descrição
            const matchesTitle = titulo.textContent.toLowerCase().includes(searchTerm.toLowerCase());
            const matchesDesc = descricao.textContent.toLowerCase().includes(searchTerm.toLowerCase());
            
            // Destaca visualmente os itens encontrados
            if (matchesTitle || matchesDesc) {
                item.style.borderLeft = '4px solid #0d6efd';
            } else {
                item.style.borderLeft = 'none';
            }
        }
    });
}

/**
 * Inicializa a validação de formulários
 */
function initFormValidation() {
    const forms = document.querySelectorAll('.needs-validation');
    
    // Adiciona validação para cada formulário
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            
            form.classList.add('was-validated');
        });
    });
}

/**
 * Animação de scroll suave para links internos
 */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        
        const targetId = this.getAttribute('href');
        if (targetId === '#') return;
        
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            targetElement.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

/**
 * Adiciona feedback visual aos botões
 */
document.querySelectorAll('.btn').forEach(button => {
    button.addEventListener('click', function() {
        // Adiciona efeito de clique
        this.classList.add('btn-clicked');
        
        // Remove o efeito após 200ms
        setTimeout(() => {
            this.classList.remove('btn-clicked');
        }, 200);
    });
});

/**
 * Função para confirmar exclusão de item
 */
function confirmDelete(itemId, itemName) {
    if (confirm(`Tem certeza que deseja excluir "${itemName}"? Esta ação não pode ser desfeita.`)) {
        // Envia o formulário de exclusão
        document.getElementById(`delete-form-${itemId}`).submit();
    }
}

/**
 * Detecta se o usuário está offline e exibe uma notificação
 */
window.addEventListener('offline', function() {
    showNotification('Você está offline. Algumas funcionalidades podem não estar disponíveis.', 'warning');
});

window.addEventListener('online', function() {
    showNotification('Conexão restabelecida!', 'success');
});

/**
 * Exibe uma notificação temporária
 */
function showNotification(message, type = 'info') {
    // Cria o elemento de notificação
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    
    // Adiciona ao corpo do documento
    document.body.appendChild(notification);
    
    // Exibe a notificação
    setTimeout(() => {
        notification.classList.add('show');
    }, 100);
    
    // Remove após 5 segundos
    setTimeout(() => {
        notification.classList.remove('show');
        
        // Remove do DOM após a animação
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 5000);
}

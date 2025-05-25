/**
 * main.js - Smart University Assistant
 */

document.addEventListener('DOMContentLoaded', function() {
    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    // Mobile menu toggle
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    
    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', function() {
            mobileMenu.classList.toggle('hidden');
        });
    }

    // Chat functionality
    initChat();
    
    // Animations on scroll
    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    
    if (animatedElements.length > 0) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-fade-in');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });
        
        animatedElements.forEach(element => {
            observer.observe(element);
        });
    }
});

/**
 * Initialize chat functionality
 */
function initChat() {
    const chatForm = document.getElementById('chat-form');
    const userInput = document.getElementById('user-message');
    const messagesContainer = document.querySelector('.messages-container');
    const loadingIndicator = document.querySelector('.typing-indicator');
    const suggestionBtns = document.querySelectorAll('.suggestion-btn');
    
    if (!chatForm) return;
    
    // Handle suggestion buttons
    if (suggestionBtns.length > 0) {
        suggestionBtns.forEach(btn => {
            btn.addEventListener('click', function() {
                const suggestionText = this.dataset.suggestion || this.textContent;
                userInput.value = suggestionText;
                chatForm.dispatchEvent(new Event('submit'));
            });
        });
    }
    
    // Handle form submission
    chatForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const message = userInput.value.trim();
        if (!message) return;
        
        // Add user message to chat
        addMessageToChat('user', message);
        
        // Clear input
        userInput.value = '';
        
        // Show loading indicator
        if (loadingIndicator) {
            loadingIndicator.classList.remove('hidden');
        }
        
        // Scroll to bottom
        scrollToBottom();
        
        // Send message to server
        sendMessage(message);
    });
    
    /**
     * Send message to server
     * @param {string} message - User message
     */
    function sendMessage(message) {
        fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            // Hide loading indicator
            if (loadingIndicator) {
                loadingIndicator.classList.add('hidden');
            }
            
            // Add assistant response to chat
            addMessageToChat('assistant', data.response);
            
            // Scroll to bottom
            scrollToBottom();
        })
        .catch(error => {
            console.error('Error:', error);
            
            // Hide loading indicator
            if (loadingIndicator) {
                loadingIndicator.classList.add('hidden');
            }
            
            // Add error message
            addMessageToChat('assistant', 'عفواً، حدث خطأ في الاتصال. يرجى المحاولة مرة أخرى.');
            
            // Scroll to bottom
            scrollToBottom();
        });
    }
    
    /**
     * Add message to chat
     * @param {string} role - 'user' or 'assistant'
     * @param {string} content - Message content
     */
    function addMessageToChat(role, content) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', `message-${role}`);
        
        if (role === 'assistant') {
            // Process markdown for assistant messages
            // Using marked.js if available, otherwise use basic formatting
            let processedContent = content;
            
            if (window.marked) {
                // Configure marked.js for RTL content
                marked.setOptions({
                    breaks: true,
                    gfm: true
                });
                
                processedContent = marked.parse(content);
            }
            
            messageDiv.innerHTML = `
                <div class="markdown-body">
                    ${processedContent}
                </div>
            `;
        } else {
            messageDiv.textContent = content;
        }
        
        messagesContainer.appendChild(messageDiv);
    }
    
    /**
     * Scroll chat to bottom
     */
    function scrollToBottom() {
        if (messagesContainer) {
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }
    }
    
    // Initial scroll to bottom
    scrollToBottom();
}

/**
 * Format date to Arabic format
 * @param {Date} date - Date object
 * @returns {string} Formatted date string
 */
function formatDateArabic(date) {
    const options = { 
        weekday: 'long', 
        year: 'numeric', 
        month: 'long', 
        day: 'numeric' 
    };
    return date.toLocaleDateString('ar-EG', options);
}

/**
 * Handle copying code blocks in chat
 * @param {HTMLElement} button - Copy button
 * @param {string} codeText - Code to copy
 */
function copyCode(button, codeText) {
    navigator.clipboard.writeText(codeText).then(() => {
        const originalText = button.textContent;
        button.textContent = 'تم النسخ!';
        button.classList.add('copied');
        
        setTimeout(() => {
            button.textContent = originalText;
            button.classList.remove('copied');
        }, 2000);
    });
}

/**
 * Add copy buttons to code blocks
 */
function addCodeCopyButtons() {
    if (!document.querySelector('.markdown-body')) return;
    
    const codeBlocks = document.querySelectorAll('.markdown-body pre code');
    
    codeBlocks.forEach((codeBlock, index) => {
        const pre = codeBlock.parentNode;
        
        // Create copy button
        const copyButton = document.createElement('button');
        copyButton.className = 'copy-code-button';
        copyButton.textContent = 'نسخ';
        
        // Add button to pre element
        pre.appendChild(copyButton);
        
        // Add click event
        copyButton.addEventListener('click', () => {
            const code = codeBlock.textContent;
            copyCode(copyButton, code);
        });
    });
}

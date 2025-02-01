document.addEventListener('DOMContentLoaded', () => {
    // Get DOM elements
    const elements = {
        dropZone: document.getElementById('drop-zone'),
        fileInput: document.getElementById('file-input'),
        uploadContent: document.querySelector('.upload-content'),
        fileInfo: document.querySelector('.file-info'),
        fileName: document.querySelector('.file-name'),
        form: document.getElementById('upload-form'),
        btnContent: document.querySelector('.btn-content'),
        loadingSpinner: document.querySelector('.loading-spinner'),
        themeToggle: document.getElementById('theme-toggle-btn'),
        browseBtn: document.querySelector('.browse-btn'),
        removeFileBtn: document.querySelector('.remove-file'),
        toast: document.getElementById('toast')
    };

    // Theme handling
    const theme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', theme);
    
    if (elements.themeToggle) {
        // Set initial icon
        elements.themeToggle.innerHTML = `<i class="fas ${theme === 'light' ? 'fa-moon' : 'fa-sun'}"></i>`;
        
        elements.themeToggle.addEventListener('click', () => {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            
            // Update icon
            elements.themeToggle.innerHTML = `<i class="fas ${newTheme === 'light' ? 'fa-moon' : 'fa-sun'}"></i>`;
        });
    }

    // File upload handling
    function handleFile(file) {
        if (!file || !elements.fileName || !elements.uploadContent || !elements.fileInfo) return;

        const validTypes = ['.heic', '.heif', '.jpg', '.jpeg', '.png', '.webp', '.bmp'];
        const fileExtension = file.name.toLowerCase().slice(file.name.lastIndexOf('.'));
        
        if (!validTypes.includes(fileExtension)) {
            showToast('Please select a valid image file (HEIC, JPEG, PNG, WEBP, or BMP).');
            return;
        }

        elements.fileName.textContent = file.name;
        elements.uploadContent.classList.add('hidden');
        elements.fileInfo.classList.remove('hidden');
    }

    // Drag and drop handlers
    if (elements.dropZone) {
        elements.dropZone.addEventListener('dragover', (e) => {
            e.preventDefault();
            elements.dropZone.classList.add('drag-over');
        });

        elements.dropZone.addEventListener('dragleave', (e) => {
            e.preventDefault();
            elements.dropZone.classList.remove('drag-over');
        });

        elements.dropZone.addEventListener('drop', (e) => {
            e.preventDefault();
            elements.dropZone.classList.remove('drag-over');
            
            if (!elements.fileInput) return;
            
            const file = e.dataTransfer.files[0];
            elements.fileInput.files = e.dataTransfer.files;
            handleFile(file);
        });
    }

    // Click to upload
    if (elements.browseBtn && elements.fileInput) {
        elements.browseBtn.addEventListener('click', () => {
            elements.fileInput.click();
        });

        elements.fileInput.addEventListener('change', (e) => {
            const file = e.target.files[0];
            handleFile(file);
        });
    }

    // Remove file
    if (elements.removeFileBtn && elements.fileInput && elements.uploadContent && elements.fileInfo) {
        elements.removeFileBtn.addEventListener('click', () => {
            elements.fileInput.value = '';
            elements.uploadContent.classList.remove('hidden');
            elements.fileInfo.classList.add('hidden');
        });
    }

    // Form submission
    if (elements.form && elements.btnContent && elements.loadingSpinner) {
        elements.form.addEventListener('submit', () => {
            elements.btnContent.classList.add('hidden');
            elements.loadingSpinner.classList.remove('hidden');
            
            // Reset the loading state after a short delay to account for the download starting
            setTimeout(() => {
                elements.btnContent.classList.remove('hidden');
                elements.loadingSpinner.classList.add('hidden');
            }, 1000);
        });
    }

    // Toast notification
    function showToast(message) {
        if (!elements.toast) return;
        
        elements.toast.textContent = message;
        elements.toast.classList.add('show');
        
        setTimeout(() => {
            elements.toast.classList.remove('show');
        }, 3000);
    }
}); 
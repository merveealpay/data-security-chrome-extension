document.addEventListener('paste', async (event) => {
    let clipboardData = event.clipboardData || window.clipboardData;
    let pastedData = clipboardData.getData('Text');

    // Send the pasted data to the backend for checking
    try {
        let response = await fetch('http://127.0.0.1:8000/check-data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ data: pastedData })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        let result = await response.json();
        if (result.warning) {
            alert(result.warning);
        }
    } catch (error) {
        console.error('Error:', error);
    }
});

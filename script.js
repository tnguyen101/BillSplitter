document.addEventListener('DOMContentLoaded', function() {
    fetch('expenses.json')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('tableBody');
            data.forEach(expense => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${expense.name}</td>
                    <td>${expense.amount}</td>
                    <td>${expense.people}</td>
                `;
                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error('Error fetching data:', error));

    
});


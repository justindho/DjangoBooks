console.log('inside index.js');


document.addEventListener('DOMContentLoaded', () => {

    // Update filtered results upon an update to the 'filter by author' selection
    document.getElementById('filter-author').onchange = () => {                

        // Initialize request
        const xhr = new XMLHttpRequest();
        const author = document.getElementById('filter-author').value;        
        const genre = document.getElementById('filter-genre').value;
        xhr.open('POST', 'query/');

        // Callback function for when request completes        
        xhr.onload = () => {

            console.log('Inside request onload');

            // Extract JSON data from request
            const response = JSON.parse(xhr.responseText);

            // Update the booklist div
            let results = ``;
            for (let i = 0; i < response.length; i++) {
                let title = response[i]['title'];
                let author = response[i]['author'];
                let genre = response[i]['genre'];
                results += `<li>` + title + ` - ` + author + ` - ` + genre + `</li>`;
            }                        
            document.getElementById('booklist').innerHTML = results;
        }        

        // Add data to send with request
        const data = new FormData();
        data.append('author', author);          
        data.append('genre', genre);      
        
        // Send request
        xhr.send(data);
        return false;
    }

    // Update filtered results upon an update to the 'filter by genre' selection
    document.getElementById('filter-genre').onchange = () => {                

        // Initialize request
        const xhr = new XMLHttpRequest();
        const author = document.getElementById('filter-author').value;        
        const genre = document.getElementById('filter-genre').value;
        xhr.open('POST', 'query/');

        // Callback function for when request completes        
        xhr.onload = () => {

            console.log('Inside request onload');

            // Extract JSON data from request
            const response = JSON.parse(xhr.responseText);

            // Update the booklist div
            let results = ``;
            for (let i = 0; i < response.length; i++) {
                let title = response[i]['title'];
                let author = response[i]['author'];
                let genre = response[i]['genre'];
                results += `<li>` + title + ` - ` + author + ` - ` + genre + `</li>`;
            }                        
            document.getElementById('booklist').innerHTML = results;
        }        

        // Add data to send with request
        const data = new FormData();
        data.append('author', author);          
        data.append('genre', genre);      
        
        // Send request
        xhr.send(data);
        return false;
    }
});
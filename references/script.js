document.addEventListener('DOMContentLoaded', function() {
    // Function to load and display JSON content
    function loadJSON() {
        let xhr = new XMLHttpRequest();

        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4 && xhr.status === 200) {
                let jsonData = JSON.parse(xhr.responseText);
                displayContent(jsonData);
            }
        };

        xhr.open('GET', 'content.json', true);
        xhr.send();
    }

    async function boldNames(inputString) {
        try {
            // Load the content of "co-applicants.txt" using Fetch API
            const coApplicantsResponse = await fetch('co-applicants.txt');
            if (!coApplicantsResponse.ok) {
              throw new Error('Error loading "co-applicants.txt": ' + coApplicantsResponse.status);
            }
            const coApplicantsData = await coApplicantsResponse.text();
            const coApplicantsNames = coApplicantsData.split('\n').map(name => name.trim());
        
            let regex = new RegExp(coApplicantsNames.join('|'), 'g');
            // Bold names of co-applicants
            inputString = inputString.replace(regex, (matchedName) => `<strong>${matchedName}</strong>`);
        
            // Load the content of "collaborators.txt" using Fetch API
            const collaboratorsResponse = await fetch('collaborators.txt');
            if (!collaboratorsResponse.ok) {
              throw new Error('Error loading "collaborators.txt": ' + collaboratorsResponse.status);
            }
            const collaboratorsData = await collaboratorsResponse.text();
            const collaboratorsNames = collaboratorsData.split('\n').map(name => name.trim());
        
            regex = new RegExp(collaboratorsNames.join('|'), 'g');
            // Bold names of collaborators
            inputString = inputString.replace(regex, (matchedName) => `<strong><em>${matchedName}</em></strong>`);
        
            return inputString;
        } catch (error) {
        console.error(error);
        return inputString; // Return the original inputString if there's an error
        }
    }

    // Function to display JSON content in the HTML
    async function displayContent(data) {
        let container = document.getElementById('json-content');
        let html = '';
        for (let entry of data) {
            boldedEntry = await boldNames(entry);
            html += boldedEntry + '<br>';
        }
        container.innerHTML = html;
    }

    // Load JSON content on page load
    loadJSON();
});
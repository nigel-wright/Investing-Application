
async function stockSearch() {
    const search = document.getElementById("search").value

    try {
        const response = await fetch(`http://127.0.0.1:3000/api/search/${search}`)

        if (response.ok) {
            const data = await response.json()
            console.log(data)
        } else {
            return `The response was NOT ok, error code: ${response.status}`
        }

    } catch(err) {
        return "There was an error in the search"
    }

}

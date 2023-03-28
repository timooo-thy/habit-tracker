function updateResetDate() {
			const dateInput = document.getElementById("date");
			const resetDateInput = document.getElementById("reset-date");
			resetDateInput.value = dateInput.value;
		}

function displayMessage(message) {
    alert(message);
}
const isEmployer = document.getElementById("id_is_corporate")
const secondNameField = document.getElementById("second_name_field")
const firstNameLabel = document.getElementById("first_name_label")
const companyNameLabel = document.getElementById("company_name_label")

function changeLabel() {
    if (companyNameLabel.style.display === "none") {
        firstNameLabel.style.display = "none"
        companyNameLabel.style.display = "inline"
        secondNameField.style.display="none"
    }
    else {
        firstNameLabel.style.display = "inline"
        companyNameLabel.style.display = "none"
        secondNameField.style.display="block"
    }
}

isEmployer.addEventListener("click", changeLabel)
function showRoleDropdown() {
    var pdfSubmissionDropdown = document.getElementById("pdfSubmissionDropdown");
    var selectedOption = document.getElementById("pdfSubmission").value;
    var dataScientistFields = document.getElementById("dataScientistFields");
    var productDesignEngineerFields = document.getElementById("productDesignEngineerFields");
    var graphicDesignEngineerFields = document.getElementById("graphicDesignEngineerFields");
    var marketingAdvisorFields = document.getElementById("marketingAdvisorFields");

    // Hide all additional fields initially
    dataScientistFields.style.display = "none";
    productDesignEngineerFields.style.display = "none";
    graphicDesignEngineerFields.style.display = "none";
    marketingAdvisorFields.style.display = "none";

    // Show additional fields based on the selected option
    if (selectedOption === "dataScientist") {
        dataScientistFields.style.display = "block";
    } else if (selectedOption === "productDesignEngineer") {
        productDesignEngineerFields.style.display = "block";
    } else if (selectedOption === "graphicDesignEngineer") {
        graphicDesignEngineerFields.style.display = "block";
    } else if (selectedOption === "marketingAdvisor") {
        marketingAdvisorFields.style.display = "block";
    }
    // Add more conditions for other options as needed

    // Rest of your code...
}
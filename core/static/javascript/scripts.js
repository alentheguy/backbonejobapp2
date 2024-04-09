function showRoleDropdown() {
    var pdfSubmissionDropdown = document.getElementById("pdfSubmissionDropdown");
    var selectedOption = document.getElementById("pdfSubmission").value;
    var dataScientistFields = document.getElementById("dataScientistFields");
    var graphicDesignEngineerFields = document.getElementById("graphicDesignEngineerFields");
    var marketingAdvisorFields = document.getElementById("marketingAdvisorFields");
    var mobileAppFields = document.getElementById("mobileAppFields"); // Add this line
    var challengeSubmission = document.getElementById("challengeSubmission");

    // Hide all additional fields initially
    dataScientistFields.style.display = "none";
    graphicDesignEngineerFields.style.display = "none";
    marketingAdvisorFields.style.display = "none";
    mobileAppFields.style.display = "none";
    challengeSubmission.style.display = "none";

    // Show additional fields based on the selected option
    if (selectedOption === "dataScientist") {
        dataScientistFields.style.display = "block";
        challengeSubmission.style.display = "block";
    } else if (selectedOption === "graphicDesigner") {
        graphicDesignEngineerFields.style.display = "block";
        challengeSubmission.style.display = "block";
    } else if (selectedOption === "SocialMedia") {
        marketingAdvisorFields.style.display = "block";
        challengeSubmission.style.display = "block";
    } else if (selectedOption === "mobileAppDev") { // Add this block
        mobileAppFields.style.display = "block";
        challengeSubmission.style.display = "block";
    }
    
    // Add more conditions for other options as needed

    // Rest of your code...
}


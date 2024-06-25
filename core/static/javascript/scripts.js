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

// document.addEventListener('DOMContentLoaded', function() {
//     const elements = document.querySelectorAll('.fadefromside.hidden');

//     const observer = new IntersectionObserver(entries => {
//         entries.forEach(entry => {
//             if (entry.isIntersecting) {
//                 entry.target.classList.add('visible');
//                 observer.unobserve(entry.target); // Stop observing the element once it has become visible
//             }
//         });
//     });

//     elements.forEach(element => {
//         observer.observe(element);
//     });
// });

document.addEventListener('DOMContentLoaded', function() {
    const elements = document.querySelectorAll('.fadefromleft');
    const windowHeight = window.innerHeight;

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            } else {
                entry.target.classList.remove('visible');
            }
        });
    }, {
        threshold: [0, 0.5, 1]
    });

    elements.forEach(element => {
        observer.observe(element);
    });

    window.addEventListener('scroll', () => {
        elements.forEach(element => {
            const elementRect = element.getBoundingClientRect();
            const elementHeight = elementRect.height;
            const elementTop = elementRect.top + window.scrollY;
            const start = elementTop - windowHeight;
            const end = elementTop + elementHeight;

            if (window.scrollY > start && window.scrollY < end) {
                const progress = (window.scrollY - start) / (end - start);
                let movement;
                if (progress < 0.25) {
                    // Move towards center
                    movement = -100 + (400 * progress);
                } else {
                    // Stay centered
                    movement = 0;
                }
                element.style.transform = `translateX(${movement}%)`;
            } else if (window.scrollY <= start) {
                element.style.transform = 'translateX(-100%)';
            }
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const elements = document.querySelectorAll('.fadefromright');
    const windowHeight = window.innerHeight;

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            } else {
                entry.target.classList.remove('visible');
            }
        });
    }, {
        threshold: [0, 0.5, 1]
    });

    elements.forEach(element => {
        observer.observe(element);
    });

    window.addEventListener('scroll', () => {
        elements.forEach(element => {
            const elementRect = element.getBoundingClientRect();
            const elementHeight = elementRect.height;
            const elementTop = elementRect.top + window.scrollY;
            const start = elementTop - windowHeight;
            const end = elementTop + elementHeight;

            if (window.scrollY > start && window.scrollY < end) {
                const progress = (window.scrollY - start) / (end - start);
                let movement;
                if (progress < 0.25) {
                    // Move towards center
                    movement = 100 - (400 * progress);
                } else {
                    // Stay centered
                    movement = 0;
                }
                element.style.transform = `translateX(${movement}%)`;
            } else if (window.scrollY <= start) {
                element.style.transform = 'translateX(100%)';
            }
        });
    });
});
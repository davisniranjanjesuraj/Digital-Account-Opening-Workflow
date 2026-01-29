// ===========================
// Select Elements
// ===========================
const landing = document.getElementById("landing");
const personal = document.getElementById("personal");
const kyc = document.getElementById("kyc");
const docs = document.getElementById("docs");
const success = document.getElementById("success");

const startBtn = document.getElementById("start-account");
const continueKycBtn = document.getElementById("continue-kyc");
const continueDocsBtn = document.getElementById("continue-docs");
const submitBtn = document.getElementById("submit");

// ===========================
// Step 1 → Step 2: Landing → Personal
// ===========================
startBtn.onclick = () => {
    landing.classList.add("hidden");
    personal.classList.remove("hidden");
};

// ===========================
// Step 2 → Step 3: Personal → KYC
// ===========================
continueKycBtn.onclick = () => {
    // Optional validation
    const name = document.getElementById("name").value.trim();
    const dob = document.getElementById("dob").value.trim();
    const email = document.getElementById("email").value.trim();
    if (!name || !dob || !email) {
        alert("Please fill all personal details.");
        return;
    }

    personal.classList.add("hidden");
    kyc.classList.remove("hidden");
};

// ===========================
// Step 3 → Step 4: KYC → Document Upload
// ===========================
continueDocsBtn.onclick = () => {
    const aadhar = document.getElementById("aadhar").value.trim();
    const pan = document.getElementById("pan").value.trim();
    if (!aadhar || !pan) {
        alert("Please fill KYC details.");
        return;
    }

    kyc.classList.add("hidden");
    docs.classList.remove("hidden");
};

// ===========================
// Step 4 → Step 5: Document Upload → Success
// ===========================
submitBtn.onclick = () => {
    const idType = document.getElementById("idType").value;
    const addressType = document.getElementById("addressType").value;
    const idFile = document.getElementById("idUpload").files[0];
    const addressFile = document.getElementById("addressUpload").files[0];

    if (!idType || !addressType || !idFile || !addressFile) {
        alert("Please select document types and upload files.");
        return;
    }

    docs.classList.add("hidden");
    success.classList.remove("hidden");
};

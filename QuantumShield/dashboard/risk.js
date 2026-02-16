function calculateRisk(state) {
    let score = 0;
    let details = [];

    // Transport security evaluation
    if (state.transport === "KEMTLS") {
        score += 50;
        details.push("KEMTLS used for transport security");
    } else {
        details.push("Non-post-quantum transport detected");
    }

    // KEM evaluation
    if (state.kem && state.kem.toLowerCase().includes("kyber")) {
        score += 25;
        details.push("NIST-standard post-quantum KEM in use");
    } else {
        details.push("Non-standard or missing KEM");
    }

    // Signature evaluation
    if (state.signature &&
        (state.signature.toLowerCase().includes("dilithium") ||
         state.signature.toLowerCase().includes("falcon"))) {
        score += 20;
        details.push("Post-quantum digital signature scheme in use");
    } else {
        details.push("Non-post-quantum signature scheme detected");
    }

    // Hash function
    if (state.hash) {
        score += 5;
        details.push("Modern cryptographic hash function configured");
    }

    return {
        score: Math.min(score, 100),
        details: details
    };
}

function riskLabel(score) {
    if (score >= 85) return "Quantum-Safe";
    if (score >= 60) return "Transitional Security";
    return "High Quantum Risk";
}

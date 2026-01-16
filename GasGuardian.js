const { ethers } = require("ethers");

async function verifyGas() {
    const provider = new ethers.providers.StaticJsonRpcProvider("https://rpc.ankr.com/eth");
    const gasPrice = await provider.getGasPrice();
    const gwei = ethers.utils.formatUnits(gasPrice, "gwei");

    console.log(`>> NETWORK TELEMETRY: CURRENT GAS IS ${parseFloat(gwei).toFixed(2)} GWEI`);

    // ARCHITECT'S LIMIT: We only strike if gas is under 25 Gwei
    // This ensures your $25 fuel lasts for high-value extractions only.
    const MAX_GWEI = 25; 

    if (parseFloat(gwei) > MAX_GWEI) {
        console.log(`>> ALERT: Gas is too high (${gwei} gwei). Aborting strike to preserve fuel.`);
        process.exit(1); // Exit with code 1 to stop the GitHub Action workflow here
    }

    console.log(">> GAS STATUS: OPTIMAL. Neural Link clear for strike.");
}

verifyGas().catch(console.error);

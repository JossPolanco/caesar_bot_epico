const { Client, LocalAuth, MessageMedia } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');
const axios = require('axios');

const client = new Client({
    authStrategy: new LocalAuth()
});

const FLASK_API = 'http://localhost:3000';

client.on('qr', (qr) => {
    qrcode.generate(qr, { small: true });
});

client.on('ready', () => {
    console.log('Client is ready!');
});

async function encryptMessage(phrase, shift) {
    try {
        const response = await axios.post(`${FLASK_API}/encrypt`, {
            phrase,
            shift: parseInt(shift)
        });
        return response.data.encrypted;
    } catch (error) {
        console.error('Error encrypting:', error);
        throw error;
    }
}

async function decryptMessage(phrase, shift) {
    try {
        const response = await axios.post(`${FLASK_API}/decrypt`, {
            phrase,
            shift: parseInt(shift)
        });
        return response.data.decrypted;
    } catch (error) {
        console.error('Error decrypting:', error);
        throw error;
    }
}

client.on("message", async (message) => {
    const messageBody = message.body.trim();

    const cipherMatch = messageBody.match(/^!cypher\s+(.+?)\s+(\d+)\s*$/i);
    const decipherMatch = messageBody.match(/^!decypher\s+(.+?)\s+(\d+)\s*$/i);

    if (messageBody.toLowerCase() === 'ping') {
        await message.reply('pong');
    }
    else if (cipherMatch) {
        try {
            const word = cipherMatch[1];
            const shift = cipherMatch[2];

            const encrypted = await encryptMessage(word, shift);
            await message.reply(`Encrypted: ${encrypted}`);
        } catch (error) {
            await message.reply('Error al encriptar el mensaje');
        }
    }
    else if (decipherMatch) {
        try {
            const word = decipherMatch[1];
            const shift = decipherMatch[2];

            const decrypted = await decryptMessage(word, shift);
            await message.reply(`Decrypted: ${decrypted}`);
        } catch (error) {
            await message.reply('Error al desencriptar el mensaje');
        }
    }
    else if (message.body.toLowerCase() === 'que') {
        const url = "https://images7.memedroid.com/images/UPLOADED574/625f4dd6290b4.jpeg";
        try {
            const media = await MessageMedia.fromUrl(url);
            await client.sendMessage(message.from, media, {
                sendMediaAsSticker: true,
                stickerAuthor: "yo",
                stickerName: "sticker"
            });
        } catch (error) {
            console.error('Error sending sticker:', error);
        }
    }
});

client.initialize();
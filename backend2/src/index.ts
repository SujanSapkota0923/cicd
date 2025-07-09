import cors from 'cors';
import dotenv from 'dotenv';
import express, { Application } from 'express';


import appRouter from './routes';
import { notFound } from './middlewares/notFound';
import { errorHandler } from './middlewares/errorHandler';

dotenv.config();

const app: Application = express();

app.use(express.json());

app.use(cors({origin: ['https://www.myapp.com/','http://192.168.44.138','https://myapp.com'],
  credentials: true,}));

app.use(appRouter);

app.use(notFound);
app.use(errorHandler);
app.get('/health', (req, res) => {
  res.status(200).send('OK');
});

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => console.log(`Server running in ${process.env.NODE_ENV} mode on port ${PORT}`));

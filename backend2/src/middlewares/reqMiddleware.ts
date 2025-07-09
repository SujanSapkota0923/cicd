import { NextFunction,Response,Request } from "express";
import { logger } from "../utils/logger";

export const reqHandler=(req:Request,res:Response,next:NextFunction) => {
    logger.info(`${req.method} ${req.url}`,{ method: req.method, url: req.url }); 
    next();
}
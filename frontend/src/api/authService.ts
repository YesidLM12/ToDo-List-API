import type { AuthResponse } from "../types/authResponse";
import type { UserLoginCredentials } from "../types/userLogin";
import type { UserRegisterCredentials } from "../types/UserRegister";

const API_URL = import.meta.env.VITE_API_URL;

export const login = async (
  credentials: UserLoginCredentials
): Promise<AuthResponse> => {
  const res = await fetch(`${API_URL}/auth/login`, {
    method: "Post",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(credentials),
  });
  if (!res.ok) throw new Error("Invalid credentials");
  return res.json();
};

export const resgisterUser = async (
  credentials: UserRegisterCredentials
): Promise<any> => {
  const res = await fetch(`${API_URL}/auth/register`, {
    method: "Post",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(credentials),
  });
  if (!res.ok) throw new Error("Error registering user");
  return res.json();
};

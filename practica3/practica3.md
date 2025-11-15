# Reporte 3  
**Instalacion del entorno y funcionamiento de la aplicacion TODO en Haskell**

## Objetivo  
Describir los pasos necesarios para:  
1. Configurar el entorno de desarrollo con Haskell y Stack.  
2. Crear e implementar una aplicación sencilla de gestión de tareas (TODO) escrita en Haskell.  
3. Ejecutar, probar y extender dicha aplicación.

---

## Requisitos previos  
- Sistema operativo compatible (Windows, macOS o Linux).  
- Conocimientos básicos de terminal o línea de comandos.  
- Familiaridad básica con Haskell.  
- Conexión a internet para descargar dependencias.

---

## Paso 1: Instalacion del entorno  

1. **Instalar GHCUP**  
    https://www.haskell.org/ghcup/

  - Entrar al PowerShell y poner el siguiente link (NO ADMIN)
    #### Set-ExecutionPolicy Bypass -Scope Process -Force;[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; try { & ([ScriptBlock]::Create((Invoke-WebRequest https://www.haskell.org/ghcup/sh/bootstrap-haskell.ps1 -UseBasicParsing))) -Interactive -DisableCurl } catch { Write-Error $_ }
#### Con esto se estas utilizando o instalando los siguientes elementos:
#### GHCup → Herramienta de instalación e entorno de desarrollo, el enlace ejecutado desacarga y realiza la instalación utilizando esta herramienta.
#### GHC → Compilador de Haskell.
#### Hugs → Interprete interactivo de Haskell.
#### HLS → Haskell Language Server, este no lo utilizan directamente. contiene las librerías estándar y código de funcionamiento de Haskell, del cual hacen uso GHC y Hugs.
#### Stack → Manejador de paquetes, similar a Pip en Python o apt en Ubuntu/Debian.
#### Cabal → Herramienta de empaquetado de binarios (buildtool), se encarga de utilizar Stack para descargar dependencias y GHC para compilar el código en un solo comando.

## Paso 2: vínculo Get Started
#### sigue la guía de inicio oficial de Haskell (vínculo Get Started) para tener una breve introducción al lenguaje y confirmar que las herramientas se instalaron correctamente.
https://www.haskell.org/get-started/
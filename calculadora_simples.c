#include <stdio.h>

int main(void){
    float num1, num2, calcular;
    int op, continuar = 1;

    while(continuar == 1){

    printf(" ------------------------\n");     
    printf("| 1 - Adição(+);         |\n| 2 - Subtração(-);      |\n| 3 - Multiplicação(*);  |\n| 4 - Divisão(/);        |\n| 0 - para sair          |\n");
    printf(" ------------------------\n");    

    printf("Deseja realizar qual operação aritmética? ");
    scanf("%d", &op);

    if(op == 0){
        break;
    }

    printf("Digite um numero: ");
    scanf("%f", &num1);

    printf("Digite outro numero: ");
    scanf("%f", &num2);

    if(op == 1){
        calcular = num1 + num2;
        printf("A soma desses números é igual a: %.2f\n",calcular); }

    else if(op == 2){
        calcular = num1 - num2;
        printf("A subtração é igual a: %.2f\n",calcular); }
     
    else if(op == 3){
        calcular = num1 * num2;
        printf("A multiplicação é igual a: %.2f\n",calcular); }
    
    else if(op == 4){
         if(num2 != 0){
                calcular = num1 / num2;
                printf("A divisão é: %.2f\n", calcular); }
            else {
                printf("Não existe divisão por zero.\n"); } }
        else {
            printf("Operação invalida!.\n"); }

            
        printf("\n1 - Continuar\n");
        printf("0 - Sair\n");
        printf("Deseja continuar? ");
        scanf("%d", &continuar);

    }

    printf("CALCULADORA ENCERRADA.\n");

    return 0; } 

